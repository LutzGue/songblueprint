import json

def find_and_replace(node):
    """
    Read JSON file, then iterates over the data to find and replace nodes based 
    on the specified conditions. It handles multiple levels of nesting, keeps the 
    'value' and 'isreplacecandidate' fields in the replaced candidate and updates the 
    'isreplaced' field to True. It deletes the 'isoriginal' field in the replaced node.
    This function is useful for manipulating hierarchical JSON data, particularly 
    to replace certain nodes based on specific criteria. The function is a recursive 
    function that operates on a node of a JSON structure.

    NEXT STEPS:
    - count iterations and stop infinite replications

    IMPORTANT: The replace candidate in curly brackets has to be the highest indent node.

    (1) This example will work:

        [rel_key_I]
            {static_harmony}
        cadence

    (2) This example will work:

        [rel_key_I]
            {static_harmony}
            cadence

    (3) This example will NOT work:

        [rel_key_I]
            {static_harmony}
                cadence

    Parameters:
    node (dict): This is a dictionary representing a node in the JSON structure. Each 
    node is expected to have the following keys: 'description', 'isreplacecandidate', 
    'isreplaced', and optionally 'children' if the node has child nodes.

    Returns:
    The function does not explicitly return a value. Instead, it modifies the input 
    JSON structure in-place. Specifically, it iterates over the data to find and replace 
    nodes based on the specified conditions. If a node is marked as a replace candidate 
    and has not been replaced yet, it replaces the 'children' of the node with those of 
    the original node with the same 'description', and updates the 'isreplaced' field 
    to True.
    """
    if node['isreplacecandidate'] and not node['isreplaced']:
        for original_node in original_nodes:
            if original_node['description'] == node['description']:
                node['children'] = original_node['children']
                node['isreplaced'] = True
    for child in node.get('children', []):
        find_and_replace(child)

# Load the data
with open('json\\output_replicate-1.json', 'r') as f:
    data = json.load(f)

# Find the original nodes
original_nodes = [node for node in data if node['isoriginal']]

# Perform the replacement
for node in data:
    find_and_replace(node)

# Save the result
with open('json\\output_replaced.json', 'w') as f:
    json.dump(data, f, indent=4)
