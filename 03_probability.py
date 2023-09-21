"""
Calculate the sum of 'value' of nested nodes in the same indent level with the same parent, 
if “isprobability” is true, and writes the total into a new key 'total'. It then adds this 
sum to a new ‘total’ field in each node and writes the updated JSON data back to the file.

LIST OF BUGS TO BE FIXED:
- not all nested values are calculated probabilities
"""

import json

def calculate_sum(node):
    total = 0
    if 'children' in node:
        for child in node['children']:
            if child['isprobability']:
                total += child['value']
        node['total'] = total
        for child in node['children']:
            calculate_sum(child)

def calculate_probability(node):
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
