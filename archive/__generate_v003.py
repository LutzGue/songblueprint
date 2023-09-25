"""
Var 1: It reads a JSON file, iterates over the nodes, and based on the ‘probability’ value, it 
uses a random function to decide whether to keep or delete nodes. If ‘isprobability’ is 
false, the entry is always retained. It starts processing from a specific node by matching 
the “description”. It removes parent nodes that are not the defined starting node but keeps 
the nested children nodes.
Var 2: The code will traverse the JSON structure, and for each node, it will check the “isprobability” field. If it’s true, it will randomly select one of the children based on their respective probabilities and remove the others. If it’s false, it will keep the node and proceed with the next nested children.
The processing will start from this node and proceed with its nested children.
"""
import json
import random

def process_node(node):
    if 'children' in node:
        if node.get('isprobability', False):
            node['children'] = [random.choices(node['children'], [child.get('probability', 0) for child in node['children']])[0]]
        for child in node['children']:
            process_node(child)

def process_json(json_data, start_node):
    for node in json_data:
        if node['description'] == start_node:
            process_node(node)

# Call the function with your JSON file and the description of the starting node
process_json('json\\output_total.json', 'phrase_major_minor')

# Print the processed JSON data
#print(json.dumps(json_data, indent=4))