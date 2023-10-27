import json
import random

def calculate_sum(node):
    """
    This function is designed to calculate the sum of the 'value' field for nodes in a hierarchical JSON structure, based on specific criteria. It operates on each node and its direct children at the same indentation level and under the same parent. 
    The function checks if the 'isprobability' field is true for each node. If true, it adds the 'value' of that node to a running total. This total represents the sum of 'value' for all nodes at the same level under the same parent where 'isprobability' is true.
    This total is then stored in a new 'total' field in the parent node. This allows each parent node to hold the sum of 'value' for its direct children where 'isprobability' is true.
    Please note that this function does not include the sum of values for grandchild nodes or nodes at lower levels in the total. It only considers direct children of each node.
    By storing this total in each parent node, this function provides a way to track and use these sums later in your code, such as for calculating probabilities or other statistics.
    This function is particularly useful when working with hierarchical JSON data and you need to calculate sums based on specific criteria. It allows you to add up values in a way that respects the structure of your data, making it easier to perform further analysis or manipulations.

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
    """
    if 'children' in node:
        total = sum(calculate_sum(child) for child in node['children'])
        node['total'] = total
    return node['value'] if node['isprobability'] else 0

def calculate_probability(node):
    """
    This function is designed to calculate the probability for each node in a hierarchical JSON structure. It operates on each node and its direct children at the same indentation level and under the same parent.
    The function calculates the probability for each child node by dividing its ‘value’ by the ‘total’ of the parent node. This is based on the assumption that the ‘total’ of a parent node represents the sum of ‘value’ for all its direct children where ‘isprobability’ is true, as calculated by a previous function.
    This calculated probability is then stored in a new ‘probability’ field in each child node. This allows each child node to hold its own probability relative to its siblings under the same parent.
    By storing this probability in each child node, this function provides a way to track and use these probabilities later in your code, such as for further statistical analysis or data manipulation.
    This function is particularly useful when working with hierarchical JSON data and you need to calculate probabilities based on specific criteria. It allows you to compute probabilities in a way that respects the structure of your data, making it easier to perform further analysis or manipulations.

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

# MODE A: 02_replicate --> 03_replace
# input_file = "json\\output_replaced.json"
# output_file = "json\\output_total.json"

# MODE B: 03_replace --> 02_replicate
generate_count = 20
randomcount = int(round(1 + (generate_count - 1) * random.random())) - 1
input_file = "json\\\modulation1\\2023\\10\\26\\2023_10_26T17_05_13\\03_replicate\\output-replicate-" + str(randomcount) + ".json"
output_file = "json\\output_total.json"

print(input_file)

# Load your JSON data
with open(input_file) as f:
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
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)
