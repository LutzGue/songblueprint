import json
import copy
import random

"""
Description: 
    This script reads a JSON file, recursively searches for specific nodes, duplicates 
    those nodes, and writes the final result back into a JSON file. The specific nodes it 
    targets are those with the properties isreplicated = false and isreplicatecandidate = true. 
    The script duplicates these nodes and their children, maintaining the original position 
    in the schema. It then sets isreplaced: true in the replaced candidate and increments 
    the value of clonenr. The final result is written into multiple JSON files.

Input:
    input_file: A string representing the path to the input JSON file.
    output_file: A string representing the path to the output JSON file.
    generate_count: count of multiple generated JSON files.

Output: 
    The function writes the final result into multiple JSON files.

        generate_count

        output_replicate-1.json
        output_replicate-2.json

Hint:
    Use INSERT command instead of APPEND command to keep the original position in the schema.

Example 1:

    Input:

        song
            lh
                item,2,8
                    note

    Explanation of the example above:

        "item,2,8" -- Parameters: 2 minimum / 8 maximum generation

Example 2:

    Input:

        song
            placeholder_a
                item_a,,2,4
                    none
            placeholder_b
                item_b,,1,7
                    note

    Result:

        ["song"["placeholder_a"["item_a"["none"]]["item_a"["none"]]["item_a"["none"]]]["placeholder_b"["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]]]

Example 3:

    Input:

        song
            item_a,,2,4
                placeholder_a
                    item_b,,1,7
                        note
    Result:

        This example will generate for item_a(1) all sub-nodes of item_b.
        (!) But for item_a(2) only item_b(1) will be generated.
        Reason: The issue with your code is that it’s modifying the list while iterating over it, 
        which can lead to unexpected behavior. When you insert a new node into the parent list, 
        it changes the indices of the subsequent elements. This can cause some elements to be 
        skipped during the iteration.

        ["song"["placeholder_a"["item_a"["placeholder_b"["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]]]["item_a"["placeholder_b"["item_b"["note"]]]]["item_a"["placeholder_b"["item_b"["note"]]]]]]
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