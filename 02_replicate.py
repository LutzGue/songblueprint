"""
This script reads a JSON file, replicates the nodes based on conditions, and writes the result to a new JSON file.

FEATURE:
    2023-09-30: 
        1) read json file. 
        2) If isReplicateCandidate == true, repeat the node and all of its nested child nodes as many times using import random and for x in range(0, int(round(generatemin + (generatemax - generatemin )*random.random()))). 
        3) Set "Isreplicated" = true in the node and write the sequential number in the 'clonenr' field. 
        4) It uses recursion to handle nested child nodes.

PARAMETERS:
JSON file.
        
RESULT:
The output will be a list of replicated nodes.
        
"""

import json
import random

import sys
sys.setrecursionlimit(20)  # Increase to a limit suitable for your needs

def replicate_node(node, clone_number=1):
    if node.get('isreplicatecandidate', False):
        min_val = node.get('generatemin', 0)
        max_val = node.get('generatemax', 0)
        num_clones = round(min_val + (max_val - min_val) * random.random())
        clones = [replicate_node(dict(node, clonenr=i+1, isreplicated=True), i+1) for i in range(num_clones)]
        return clones
    else:
        new_children = []
        for child in node.get('children', []):
            new_children.extend(replicate_node(child, clone_number))
        return [dict(node, children=new_children, clonenr=clone_number)]

def process_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
        replicated_data = [replicate_node(item) for item in data]
    else:
        replicated_data = replicate_node(data)
    with open('json\\output_replicate.json', 'w') as f:
        json.dump(replicated_data, f, indent=4)

process_json('json\\output.json')
