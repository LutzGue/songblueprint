import json
import random

# Function to process a node and its children
def process_node(node):
    """
    This function is designed to process a JSON file, starting from a node specified by the variable starting_node. The code first reads the JSON file and identifies the starting node based on its description. It then iterates over each element in the JSON structure, starting from the defined node and proceeding with its nested children nodes.
    For each node, it checks the isprobability field. If isprobability is true, it creates a probability distribution based on the probability values of the node’s children. It then uses Python’s built-in random.choices function to select one child based on this distribution, and removes all other children from the node. If isprobability is false, the node is always retained, and its children are processed in the same manner.
    The code continues this process recursively for all nested children nodes, ensuring that at each level, only one child is selected based on its defined probabilities or have isprobability set to false.
    Once all nodes have been processed in this way, the modified JSON data is written back to the original file. This ensures that the final JSON structure only contains nodes that have been selected based on their defined probabilities or have isprobability set to false.
    
    Parameters:
    node: A dictionary representing a node in the JSON structure. Each node is expected to have a 'children' field containing a list of child nodes. Each child node is a dictionary that may contain an 'isprobability' field (a boolean) and a 'probability' field (a float).

    Return:
    The function does not return any value. Instead, it modifies the 'children' field of the input node in-place.
    """
    if 'children' in node:
        # Separate the children into those with 'isprobability' true and false
        prob_children = [child for child in node['children'] if child.get('isprobability', False)]
        non_prob_children = [child for child in node['children'] if not child.get('isprobability', False)]
        if prob_children:
            probabilities = [child['probability'] for child in prob_children]
            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]
            chosen_child = random.choices(prob_children, weights=probabilities, k=1)[0]
            # Keep the chosen child and all non-probability children
            node['children'] = non_prob_children + [chosen_child]
        # Recursively process all children
        for child in node['children']:
            process_node(child)

# Load the data from the JSON file
with open('json\\modulation4\\2023\\11\\15\\2023_11_15T18_56_01\\04_probability\output-probability-1.json', 'r') as f:
    data = json.load(f)

# Define the starting node
starting_node = 'SONG'

# Find and keep only the element with the description matching the starting node
data = [element for element in data if element['description'] == starting_node]

# If the starting node was found
if data:
    element = data[0]  # Get the first (and only) element
    # Process this node and all its children
    process_node(element)

# Save the modified data back to the JSON file
with open('json\\output_generate.json', 'w') as f:
    json.dump(data, f, indent=4)
