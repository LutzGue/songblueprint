import json
import copy
import random

"""
open json file.
use recursive function.
search for isreplicated = false and isreplicatecandidate = true in all nested nodes.
create duplicate of the original node and insert clone in the same indent level as the original.
the duplicate should contain all nested childrens.
write final result into json file.

example input json:

song
   lh
      item_a
         isreplicated = false
         isreplicatecandidate = true
         cloneid = 1
         note_a
            note_a_children_1
               note_a_children_2
   rh
      item_b
         isreplicated = false
         isreplicatecandidate = true
         cloneid = 1
         note_b
            note_b_children_1
               note_b_children_2
expected result json:

song
   lh
      item_a
         isreplicated = true
         isreplicatecandidate = true
         cloneid = 1
         note_a
            note_a_children_1
               note_a_children_2
      item_a
         isreplicated = true
         isreplicatecandidate = true
         cloneid = 2
         note_a
            note_a_children_1
               note_a_children_2
   rh
      item_b
         isreplicated = true
         isreplicatecandidate = true
         cloneid = 1
         note_b
            note_b_children_1
               note_b_children_2
      item_b
         isreplicated = true
         isreplicatecandidate = true
         cloneid = 2
         note_b
            note_b_children_1
               note_b_children_2
"""

def recursive_clone(node):
    if (node.get('isreplicatecandidate', False) and not node.get('isreplicated', False)):

        # fix to avoid endless recursion
        node['isreplicated'] = True

        # calculate number of generated clones by chance
        generatemin = node['generatemin']
        generatemax = node['generatemax']
        randomcount = int(round(generatemin + (generatemax - generatemin ) * random.random())) - 1
        
        for i in range(randomcount):
            new_node = copy.deepcopy(node)
            new_node['clonenr'] += 1

            # create new clones containing nested childrens
            node['children'].insert(0, new_node)

    for child in node.get('children', []):
        recursive_clone(child)

# Load the data from the JSON file
with open('json\\output.json', 'r') as f:
    data = json.load(f)

# usage (recursive)
for node in data:
    recursive_clone(node)

# Write the result back to the JSON file
with open('json\\output_replicate.json', 'w') as f:
    json.dump(data, f, indent=4)
