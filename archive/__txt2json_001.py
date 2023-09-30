import json

def text_to_json(file_path):
    """
    Convert a text file with indentation to a nested JSON structure.
    This script is useful for converting structured text files into a hierarchical JSON format.
    If the label is between { }, it is considered as a replace candidate and isreplacecandidate 
    is set to True, otherwise False. If a value is present, it is converted to an integer and 
    isprobability is set to True, otherwise False. If the node is in the first level hierarchy, 
    isoriginal is set to True, otherwise False.

    Parameters:
    file_path (str): This is the path to the input text file that needs to be converted into 
    a JSON structure.

    Returns:
    The function returns a dictionary which represents the root of the resulting JSON 
    structure. If an error occurs during the processing of the file, the function will 
    print an error message and return None.
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
                else:
                    node['isreplacecandidate'] = False
                    node['isreplaced'] = False
                
                if value:
                    node['value'] = int(value)
                    node['isprobability'] = True
                else:
                    node['value'] = -1
                    node['isprobability'] = False

                # Add 'original' = True if node is in first level hierarchy
                if indent == 0:
                    node['isoriginal'] = True
                else:
                    node['isoriginal'] = False

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
json_data = text_to_json('txt\\phrase4.txt')
if json_data is not None:
    with open('json\\output.json', 'w') as f:
        json.dump(json_data, f, indent=4)