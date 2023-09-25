
import json

def json_to_tree(json_obj):
    """
    Converts a JSON object to a parse tree using square brackets and inverted commas. This code assumes that each node in the JSON object has a “description” field and an optional “children” field.
    This code will print each top-level object in the JSON array as a separate tree. 
    """
    tree_str = '"' + json_obj['description'] + '"'
    if 'children' in json_obj:
        tree_str += '[' + ']['.join(json_to_tree(child) for child in json_obj['children']) + ']'
    return tree_str

# Load the data from the JSON file
with open('json\\output_generate.json', 'r') as f:
    json_obj = json.load(f)

for obj in json_obj:
    print('[' + json_to_tree(obj) + ']')
