"""
read JSON file, then iterates over the data to find and replace nodes based 
on the specified conditions. 
- Handles multiple levels of nesting.
- Keeps the ‘value’ and ‘isreplacecandidate’ fields in the replaced candidate 
  and updates the ‘isreplaced’ field to True.
- Deletes the ‘isoriginal’ field in the replaced node.
"""

import json

def find_and_replace(node):
    if node['isreplacecandidate'] and not node['isreplaced']:
        for original_node in original_nodes:
            if original_node['description'] == node['description']:
                node['children'] = original_node['children']
                node['isreplaced'] = True
    for child in node.get('children', []):
        find_and_replace(child)

# Load the data
with open('json\\output.json', 'r') as f:
    data = json.load(f)

# Find the original nodes
original_nodes = [node for node in data if node['isoriginal']]

# Perform the replacement
for node in data:
    find_and_replace(node)

# Save the result
with open('json\\output_replaced.json', 'w') as f:
    json.dump(data, f, indent=4)
