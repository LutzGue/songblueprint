"""
This script reads a JSON file, replicates the nodes based on conditions, and writes the result to a new JSON file.

FEATURE:
    2023-09-30: 
        1) read json file. 
        2) If isReplicateCandidate == true, repeat the node and all of its nested child nodes as many times using import random and for x in range(0, int(round(generatemin + (generatemax - generatemin )*random.random()))). 
        3) Set "Isreplicated" = true in the node and write the sequential number in the 'clonenr' field. 
        4) It uses recursion to handle nested child nodes.
        5) Add the duplicated node at the same level as the original node, not as a child of the original node.
        6) This argument keeps track of the parent of the current node. If the current node is a replicate candidate, we append the new node to the parent (if it’s a list) instead of appending it to the current node’s children. This will add the duplicated node at the same level as the original node.
        7) It's important to keep the original position of the node with the description “mini_cadence” and add the replicated nodes “item” before it.

PARAMETERS:
JSON file.
        
RESULT:
The output will be a list of replicated nodes.
        
"""

"""
import json
import copy
import random

# Load the data from the JSON file
with open('json\\output.json', 'r') as f:
    data = json.load(f)

# Perform the transformation
for item in data:
    if item['description'] == 'dynamic_harmony':
        original_children = item['children'].copy()
        for original_child in original_children:
            if original_child['description'] == 'item' and original_child['isreplicatecandidate']:
                generatemin = original_child['generatemin']
                generatemax = original_child['generatemax']
                randomcount = int(round(generatemin + (generatemax - generatemin ) * random.random())) - 1
                for i in range(randomcount):
                    new_child = copy.deepcopy(original_child)
                    new_child['isreplicated'] = True
                    new_child['clonenr'] = i
                    item['children'].append(new_child)

# Write the result back to the JSON file
with open('json\\output_replicate.json', 'w') as f:
    json.dump(data, f, indent=4)
"""
"""
import json
import copy
import random

# Recursive function to handle nested child nodes
def handle_children(node):
    if node.get('isreplicatecandidate', False):
        generatemin = node['generatemin']
        generatemax = node['generatemax']
        randomcount = int(round(generatemin + (generatemax - generatemin ) * random.random())) - 1
        for i in range(randomcount):
            new_child = copy.deepcopy(node)
            new_child['isreplicated'] = True
            new_child['clonenr'] = i
            node['children'].append(new_child)
    for child in node.get('children', []):
        handle_children(child)

# Load the data from the JSON file
with open('json\\output.json', 'r') as f:
    data = json.load(f)

# Perform the transformation
for item in data:
    handle_children(item)

# Write the result back to the JSON file
with open('json\\output_replicate.json', 'w') as f:
    json.dump(data, f, indent=4)
"""

import json
import copy
import random

# Load the data from the JSON file
with open('json\\output.json', 'r') as f:
    data = json.load(f)

# Perform the transformation
for item in data:
    #if item['description'] == 'dynamic_harmony':
        original_children = item['children'].copy()
        for original_child in original_children:
            #if original_child['description'] == 'item' and 
            if original_child['isreplicatecandidate']:
                generatemin = original_child['generatemin']
                generatemax = original_child['generatemax']
                randomcount = int(round(generatemin + (generatemax - generatemin ) * random.random())) - 1
                for i in range(randomcount):
                    new_child = copy.deepcopy(original_child)
                    new_child['isreplicated'] = True
                    new_child['clonenr'] = i
                    item['children'].insert(item['children'].index(original_child)+i+1, new_child)

# Write the result back to the JSON file
with open('json\\output_replicate.json', 'w') as f:
    json.dump(data, f, indent=4)
