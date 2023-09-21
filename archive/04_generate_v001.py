"""
This script will traverse the JSON structure based on the probability chain and concatenate 
descriptions. If “isprobability” is False, the description of the node will be part of the 
output. The inherent layers in the JSON structure are kept for output.

!!!TODOS:
- the chain containing values -1 are missing
- output stucture has to be original json schema
- possible solution: REDESIGN -- drop in json schema rnd not choosen items
"""

import json
import random

def find_start(data, start):
    for item in data:
        if item['description'] == start:
            return item
        if 'children' in item:
            result = find_start(item['children'], start)
            if result is not None:
                return result
    return None

def traverse(node, path=[]):
    if not node.get('isprobability', False):
        path.append(node['description'])
    if 'children' in node:
        next_node = random.choices(node['children'], 
                                   weights=[child.get('probability', 1) for child in node['children']])[0]
        traverse(next_node, path)
    return path

with open('json\\output_total.json') as f:
    data = json.load(f)

start_description = 'cadV'
start_node = find_start(data, start_description)

if start_node is not None:
    output = traverse(start_node)
    print(' -> '.join(output))
else:
    print(f"No node with description '{start_description}' found.")
