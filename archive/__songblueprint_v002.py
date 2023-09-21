import json

def text_to_json(file_path):
    """
    Convert a text file with indentation to a nested JSON structure.

    Parameters:
    file_path (str): The path to the input text file.

    Returns:
    dict: The root of the resulting JSON structure.
    """
    try:
        # Initialize the root of the JSON structure and a dictionary to keep track of the current node at each indentation level
        root = []
        levels = {0: root}

        # Open the input file
        with open(file_path, 'r') as f:
            # Process each line in the file
            for line in f:
                # Determine the indentation level of the current line
                indent = len(line) - len(line.lstrip())

                # Split the line into a label and a value (if present)
                label, _, value = line.strip().partition(',')

                # Create a new node with the label and value
                node = {'description': label}

                if '{' in label or '}' in label:
                    node['description'] = label.replace('{', '').replace('}', '')
                    node['isreplacecandidate'] = True
                    node['isreplaced'] = False
                    # node['replacedbyoriginal'] = label.replace('{', '').replace('}', '')
                if value:
                    node['value'] = int(value)

                # Add 'original' = True if node is in first level hierarchy
                if indent == 0:
                    node['isoriginal'] = True

                # Add the new node to the current level in the JSON structure
                levels[indent].append(node)

                # Update the current node at this indentation level and all higher levels
                levels[indent + 4] = node.setdefault('children', [])

        # Remove empty 'children' nodes
        def remove_empty_children(node):
            if 'children' in node and not node['children']:
                del node['children']
            else:
                for child in node.get('children', []):
                    remove_empty_children(child)

        for node in root:
            remove_empty_children(node)

        return root

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# usage
json_data = text_to_json('txt\\phrase1.txt')
if json_data is not None:
    with open('output.json', 'w') as f:
        json.dump(json_data, f, indent=4)

# --------------------------------------------------
# read JSON file, then iterates over the data to find and replace nodes based 
# on the specified conditions. 
# - Handles multiple levels of nesting.
# - Keeps the ‘value’ and ‘isreplacecandidate’ fields in the replaced candidate 
#   and updates the ‘isreplaced’ field to True.
# - Deletes the ‘isoriginal’ field in the replaced node.

# Load the data from the JSON file
with open('output.json') as f:
    data = json.load(f)

# Function to find a node by description
def find_node(description, data):
    for node in data:
        #if node['description'] == description and 'isoriginal' in node and node['isoriginal'] == True:
        if node['description'] == description and node['isoriginal'] == True:
            return node
    return None

# Function to replace nodes recursively
def replace_nodes(node, indent):
    if 'children' in node:
        for child in node['children']:
            # Check if the child node should be replaced
            if child.get('isreplacecandidate', False) and not child.get('isreplaced', False):
                # Find the original node with the same description
                original_node = find_node(child['description'], data)
                if original_node is not None:
                    # Keep the 'value' and 'isreplacecandidate' fields in the replaced candidate, if they exist
                    value = child.get('value', None)
                    isreplacecandidate = child.get('isreplacecandidate', False)

                    # Find the child node that will be replaced.
                    child_index = node['children'].index(child)

                    # Replace the child node with the original node and its children
                    node['children'][child_index] = original_node

                    # Update the 'value', 'isreplacecandidate', and 'isreplaced' fields in the replaced candidate, if they exist
                    if value is not None:
                        node['children'][child_index]['value'] = value
                    if isreplacecandidate:
                        node['children'][child_index]['isreplacecandidate'] = isreplacecandidate
                    node['children'][child_index]['isreplaced'] = True

                    # Delete the 'isoriginal' field in the replaced candidate, if it exists
                    if 'isoriginal' in node['children'][child_index] and indent > 0:
                        dummy = 1
                        # del node['children'][child_index]['isoriginal']

            replace_nodes(child, indent+1)

# Iterate over the data
for node in data:
    replace_nodes(node, 0)

# Save the modified data back to the JSON file
with open('output_replaced.json', 'w') as f:
    json.dump(data, f, indent=4)