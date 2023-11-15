
import json

def json_to_tree(json_obj):
    """
    Converts a JSON object to a parse tree using square brackets and inverted commas. This code assumes that each node in the JSON object has a “description” field and an optional “children” field.
    This code will print each top-level object in the JSON array as a separate tree.

    Parameters:
    json_obj (dict): A dictionary representing a node in the JSON object. 
    This dictionary should have a 'description' key representing the node's value,
    and optionally a 'children' key with a list of dictionaries representing the node's children.
    
    Returns:
    str: A string representation of the parse tree rooted at json_obj, using square brackets and inverted commas.
    
    The parsing tree syntax provides a structured representation of the grammatical construction of a phrase or sentence. An example of a generated parsing tree syntax is as follows:
    
    ["phrase_major_minor"["phrase_major"["meta"["key_major"["e"]]["meter"["6/4"]]]["song"["start"]["conn"]["end"]]]]
    
    This syntax represents a hierarchical structure where “phrase_major_minor” is the root node, and it has a child “phrase_major”. The “phrase_major” node further has two children: “meta” and “song”. The “meta” node itself has two children: “key_major”, which has a child “e”, and “meter”, which has a child “6/4”. The “song” node has three children: “start”, “conn”, and “end”.
    To visualize this parsing tree, you can use the jsSyntaxTree tool available at:
    
    http://www.ironcreek.net/syntaxtree/
    
    This tool generates an image of the syntax tree based on the provided syntax. Simply paste the syntax into the text box on the jsSyntaxTree webpage and press ‘Draw’ to generate the image. This can be particularly useful for understanding complex sentence structures or for educational purposes.
    
    """
    tree_str = '"' + json_obj['description']
    if json_obj['isreplicatecandidate']:
        tree_str += '(' + str(json_obj['clonenr']) + ')'
    tree_str += '"'
    if 'children' in json_obj:
        tree_str += '[' + ']['.join(json_to_tree(child) for child in json_obj['children']) + ']'
    return tree_str

# Load the data from the JSON file
with open('json\\output_generate.json', 'r') as f:
#with open('json\\secondary1\\2023\\11\\11\\2023_11_11T18_38_43\\05_generate\\output-generate-1-2.json', 'r') as f:
#with open('json\\modulation4\\2023\\11\\15\\2023_11_15T17_46_40\\03_replicate\\output-replicate-1.json', 'r') as f:

# with open('json\\output_generate.json', 'r') as f:
    json_obj = json.load(f)

for obj in json_obj:
    print('[' + json_to_tree(obj) + ']')
