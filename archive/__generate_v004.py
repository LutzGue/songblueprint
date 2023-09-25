"""
Var 1: It reads a JSON file, iterates over the nodes, and based on the ‘probability’ value, it 
uses a random function to decide whether to keep or delete nodes. If ‘isprobability’ is 
false, the entry is always retained. It starts processing from a specific node by matching 
the “description”. It removes parent nodes that are not the defined starting node but keeps 
the nested children nodes.
Var 2: The code will traverse the JSON structure, and for each node, it will check the “isprobability” field. If it’s true, it will randomly select one of the children based on their respective probabilities and remove the others. If it’s false, it will keep the node and proceed with the next nested children.
The processing will start from this node and proceed with its nested children.
Var 3: It reads a JSON file, iterates over each element, and based on the probability distribution in the “children” node, it selects one item and removes the others.
The built-in random.choices function to select one item based on the provided probability distribution. The selected item is then kept in the ‘children’ field, while all other items are removed. The modified data is then written back to the JSON file.
You can define the starting node in the first level as a variable. 
"""
import json
import random

# Define the starting node
starting_node = 'interval_3k'

# Load the data from the JSON file
with open('json\\output_total.json', 'r') as f:
    data = json.load(f)

# Iterate over each element in the data
for element in data:
    # Check if the element's description matches the starting node
    if element['description'] == starting_node:
        # Check if the element has a 'children' field
        if 'children' in element:
            # Create a list of probabilities
            probabilities = [child['value'] for child in element['children']]
            # Normalize the probabilities
            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]
            print(probabilities, total)
            # Choose one child based on the probability distribution
            chosen_child = random.choices(element['children'], weights=probabilities, k=1)[0]
            print(chosen_child)
            # Remove all children except for the chosen one
            element['children'] = [chosen_child]

# Save the modified data back to the JSON file
with open('json\\output_generated.json', 'w') as f:
    json.dump(data, f, indent=4)
