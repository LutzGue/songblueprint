import json
import copy
import random

"""
It reads a JSON file, recursively searches for nodes with isreplicated = false and isreplicatecandidate = true, duplicates those nodes, and writes the final result back into a JSON file.

PROCESS:
1) open json file.
2) use recursive function to search in all nested nodes / children.
3) search for node with condition (isreplicated = false AND isreplicatecandidate = true) in all nested nodes.
4) create duplicate of the original node and insert clone in the same indent level as the original.
5) the duplicate should contain all nested childrens as in the original.
6) use INSERT command instead of APPEND command to keep the original position in the schema.
7) set value in replaced candidate to isreplaced: true.
8) increase the value of clonenr.
9) write final result into json file. generate multiple schema files.

Example:

song
    lh
        item,2,8
            note

Explanation of the example above:

    "item,2,8": 2 minimum / 8 maximum generation

"""

def recursive_search(node, parent=None, key=None):
    if isinstance(node, dict):
        if node.get('isreplicated') == False and node.get('isreplicatecandidate') == True:
            # Calculate number of generated clones by chance
            generatemin = node.get('generatemin', 0)
            generatemax = node.get('generatemax', 0)
            randomcount = int(round(generatemin + (generatemax - generatemin) * random.random())) - 1

            # Create duplicates of the node
            for i in range(randomcount):
                new_node = copy.deepcopy(node)
                new_node['isreplicated'] = True
                new_node['clonenr'] += i + 1

                # Insert the duplicate node at the same indent level as the original
                parent.insert(key + i + 1, new_node)

        for k, v in node.items():
            recursive_search(v, node, k)

    elif isinstance(node, list):
        for i in range(len(node)):
            recursive_search(node[i], node, i)

def process_json_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    recursive_search(data)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# edit user defined parameters here
input_filename = 'json\\output.json'
output_filename_syntax = 'json\\output_replicate-'
generate_count = 10

# Call the function with your input and output file paths. generate different schemas.
for n in range(generate_count):
   output_filename_number = output_filename_syntax + str(n+1) + '.json'
   process_json_file(input_filename, output_filename_number)
