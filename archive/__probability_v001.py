"""
Calculate the sum of 'value' of nested nodes in the same indent level with the same parent, 
if “isprobability” is true, and writes the total into a new key 'total'. It then adds this 
sum to a new ‘total’ field in each node and writes the updated JSON data back to the file.
"""

import json

def calculate_sum(node):
    total = 0
    if 'children' in node:
        for child in node['children']:
            if child['isprobability']:
                total += child['value']
        total += calculate_sum(child)
        node['total'] = total
    return total

# Load your JSON data
with open('output_replaced.json') as f:
    data = json.load(f)

# Check if data is a list
if isinstance(data, list):
    for item in data:
        calculate_sum(item)
else:
    calculate_sum(data)

# Write the updated data back to the file
with open('output_total.json', 'w') as f:
    json.dump(data, f, indent=4)
