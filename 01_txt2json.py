import json

def text_to_json(file_path):
    """
    Convert a text file with indentation to a nested JSON structure.
    This script is useful for converting structured text files into a hierarchical JSON format.
    If the label is between { }, it is considered as a replace candidate and isreplacecandidate 
    is set to True, otherwise False. If a value is present, it is converted to an integer and 
    isprobability is set to True, otherwise False. If the node is in the first level hierarchy, 
    isoriginal is set to True, otherwise False.

    Features implemented:
    - 2023-09-30: Extend the parsing from 1 comma separated value to 3 comma separated values. 
      The first parameter is 'value'. the second parameter is 'generatemin' and the third is 
      'generatemax'. set 'isreplicated' = true. in case of missing values replace value with -1 
      and set 'isreplicated' = false and 'isreplicatecandidate' = true.
    - 2023-10-17: Comment out sections in TXT using # character and ignoring blank lines in TXT.

    Parameters:
    - file_path (str): This is the path to the input text file that needs to be converted into 
    a JSON structure.
    - debugmode (boolean)
    - output_filename (str)

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

                # Filter out comment lines and empty rows in TXT
                if (len(line.strip()) > 0 and line.strip()[:1] != '#'):

                    # Determine the indentation level of the current line
                    indent = len(line) - len(line.lstrip())

                    # Split the line into a label and a value (if present)
                    parts = line.strip().split(',')
                    
                    label = parts[0]

                    value = int(parts[1]) if len(parts) > 1 and parts[1] else -1
                    generatemin = int(parts[2]) if len(parts) > 2 and parts[2] else -1
                    generatemax = int(parts[3]) if len(parts) > 3 and parts[3] else -1

                    # DEBUGGING
                    if is_mode_debugging:
                        print(indent, label, value, generatemin, generatemax)

                    # Create a new node with the label and value
                    node = {'description': label}

                    # type: replacement
                    if '{' in label or '}' in label:
                        node['description'] = label.replace('{', '').replace('}', '')
                        node['isreplacecandidate'] = True
                        node['isreplaced'] = False
                    else:
                        node['isreplacecandidate'] = False
                        node['isreplaced'] = False

                    # type: probability value
                    node['value'] = value

                    if value != -1:
                        node['isprobability'] = True
                    else:
                        node['isprobability'] = False

                    # type: generate replications
                    node['generatemin'] = generatemin
                    node['generatemax'] = generatemax

                    node['isreplicated'] = False
                    node['clonenr'] = 1

                    if generatemin != -1 and generatemax != -1:
                        node['isreplicatecandidate'] = True
                        node['isreplicated'] = False
                    else:
                        node['isreplicatecandidate'] = False
                        node['isreplicated'] = False

                    # Add 'original' = True if node is in first level hierarchy
                    if indent == 0:
                        node['isoriginal'] = True
                    else:
                        node['isoriginal'] = False

                    # Add the new node to the current level in the JSON structure
                    levels[indent].append(node)

                    # Update the current node at this indentation level and all higher levels
                    levels[indent + 4] = node.setdefault('children', [])

                else:
                    # DEBUGGING
                    if is_mode_debugging:
                        print('skip comment or empty line:', '"' + line + '"')

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

# edit user defined parameters here
is_mode_debugging = False
input_filename = 'txt\\reharmonization2.txt'
output_filename = 'json\\output.json'

# call function
json_data = text_to_json(input_filename)

# store json file
if json_data is not None:
    with open(output_filename, 'w') as f:
        json.dump(json_data, f, indent=4)