"""
It reads a JSON file, iterates over the nodes, and based on the ‘probability’ value, it 
uses a random function to decide whether to keep or delete nodes. If ‘isprobability’ is 
false, the entry is always retained. It starts processing from a specific node by matching 
the “description”. It removes parent nodes that are not the defined starting node but keeps 
the nested children nodes.
"""
import json
import random

def process_node(node, start_node):
    if node['description'] == start_node:
        if 'children' in node:
            node['children'] = [process_node(child, start_node) for child in node['children']]
            node['children'] = [child for child in node['children'] if child is not None]
        return node
    else:
        if 'isprobability' in node and node['isprobability']:
            if random.random() < node.get('probability', 0):
                if 'children' in node:
                    node['children'] = [process_node(child, start_node) for child in node['children']]
                    node['children'] = [child for child in node['children'] if child is not None]
                return node
        else:
            if 'children' in node:
                node['children'] = [process_node(child, start_node) for child in node['children']]
                return node

def process_json(json_file, start_node):
    with open(json_file, 'r') as f:
        data = json.load(f)

    processed_data = process_node(data[0], start_node)

    with open('json\\output_generated.json', 'w') as f:
        json.dump(processed_data, f, indent=4)

# Call the function with your JSON file and the description of the starting node
process_json('json\\output_total.json', 'interval_3k_4k')
