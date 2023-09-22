import json

def calculate_sum(node):
    """
    Calculate the sum of 'value' of nested nodes in the same indent level with the same parent, 
    if 'isprobability' is true, and writes the total into a new key 'total'. It then adds this 
    sum to a new 'total' field in each node. it sums up the values of all descendant nodes, 
    not just direct children. It writes the updated JSON data back to the file.
    These functions are useful for manipulating hierarchical JSON data, particularly when 
    to calculate sums and probabilities based on specific criteria.

    Parameters:
    node (dict): This is a dictionary representing a node in the JSON structure. Each node 
    is expected to have the following keys: 'value', 'isprobability', and optionally 
    'children' if the node has child nodes.

    Returns:
    The functions do not explicitly return a value. Instead, they modify the input JSON 
    structure in-place. Specifically, calculate_sum(node) calculates the sum of 'value' of 
    nested nodes in the same indent level with the same parent, if 'isprobability' is true, 
    and writes the total into a new key 'total'. It then adds this sum to a new 'total' 
    field in each node.

    !!! LIST OF BUGS TO BE FIXED:
    - not all nested values are calculated probabilities
    """
    total = 0
    if 'children' in node:
        for child in node['children']:
            if child['isprobability']:
                total += child['value']
        node['total'] = total
        for child in node['children']:
            calculate_sum(child)

def calculate_probability(node):
    """
    The formular for calculating the 'probability' is the 'value' divided by 'total'. 
    It writes the updated JSON data back to the file.

    Parameters:
    node (dict): This is a dictionary representing a node in the JSON structure. Each node 
    is expected to have the following keys: 'value', 'isprobability', and optionally 
    'children' if the node has child nodes.

    Returns:
    The functions do not explicitly return a value. Instead, they modify the input JSON 
    structure in-place. Specifically calculate_probability(node) calculates the probability 
    for each node by dividing the 'value' by the 'total' and writes this into a new 
    'probability' field in each node.
    """
    if 'children' in node:
        for child in node['children']:
            if child['isprobability'] and 'total' in node and node['total'] != 0:
                child['probability'] = child['value'] / node['total']
            calculate_probability(child)

# Load your JSON data
with open('json\\output_replaced.json') as f:
    data = json.load(f)

# Check if data is a list
if isinstance(data, list):
    for item in data:
        calculate_sum(item)
        calculate_probability(item)
else:
    calculate_sum(data)
    calculate_probability(data)

# Write the updated data back to the file
with open('json\\output_total.json', 'w') as f:
    json.dump(data, f, indent=4)
