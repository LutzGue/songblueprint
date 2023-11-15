import json
import os
import datetime
import logging
import copy
import random

def file_management(parameters):

    if parameters["debug"]["is_active"]:
        print("--- MODULE: file_management ---")

    # initial global variables for function return
    project = {
        "general":{
            "project_path":""
        },
        "txt_to_json":{
            "input_file":"",
            "output_file":""
        },
        "replace":{
            "input_file":"",
            "output_file":""
        },
        "replicate":{
            "input_file":"",
            "output_file":""
        },
        "probability":{
            "input_file":"",
            "output_file":""
        },
        "generate":{
            "input_file":"",
            "output_file":""
        }        
    }

    # timestamp
    ft = "%Y_%m_%dT%H_%M_%S"
    current_timestamp = datetime.datetime.now().strftime(ft)
    current_year = datetime.datetime.now().strftime("%Y")
    current_month = datetime.datetime.now().strftime("%m")
    current_day = datetime.datetime.now().strftime("%d")

    if parameters["debug"]["is_active"]:
        print('tmsp:',current_timestamp)

    # --------------------------------
    # create project folder
    # --------------------------------

    try:
        project_general_path = ""   # init
        project_general_path = parameters["project"]["project_path"]

        if parameters["debug"]["is_active"]:
            print("general_path:",project_general_path)

        project_name = ""   # init
        if parameters["project"]["create_project_folder"]:
            if parameters["project"]["project_name"] == "DEFAULT":
                str1 = parameters["module"]["01_txt_to_json"]["input_file"]
                str2 = os.path.basename(str1)
                project_name = os.path.splitext(str2)[0]
            else:
                project_name = parameters["project"]["project_name"]

        project_path = ""   # init
        project_path = project_general_path + '/' + project_name

        if parameters["debug"]["is_active"]:
            print("project_path:",project_path)

        try:
            os.mkdir(project_path)

            if parameters["debug"]["is_active"]:
                print("Folder %s created!" % project_path)
        except FileExistsError:
            if parameters["debug"]["is_active"]:
                print("Folder %s already exists" % project_path)

    except Exception as e:
        print("An error occurred -- create project folder:", str(e))

    # --------------------------------
    # create date Y/M/D folders
    # --------------------------------

    try:
        if parameters["debug"]["is_active"]:
            print('previous path:',project_path)

        if parameters["project"]["create_date_folder"]:

            path_to_year = project_path + '/' + current_year
            path_to_month = path_to_year + '/' + current_month
            path_to_day = path_to_month + '/' + current_day

            project_path = path_to_day

            try:
                os.mkdir(path_to_year)
                if parameters["debug"]["is_active"]:
                    print("Folder %s created!" % path_to_year)
            except FileExistsError:
                if parameters["debug"]["is_active"]:
                    print("Folder %s already exists" % path_to_year)

            try:
                os.mkdir(path_to_month)
                if parameters["debug"]["is_active"]:
                    print("Folder %s created!" % path_to_month)
            except FileExistsError:
                if parameters["debug"]["is_active"]:
                    print("Folder %s already exists" % path_to_month)

            try:
                os.mkdir(path_to_day)
                if parameters["debug"]["is_active"]:
                    print("Folder %s created!" % path_to_day)
            except FileExistsError:
                if parameters["debug"]["is_active"]:
                    print("Folder %s already exists" % path_to_day)

    except Exception as e:
        print("An error occurred -- create date folder:", str(e))

    # --------------------------------
    # create timestamp folder
    # --------------------------------

    try:
        if parameters["debug"]["is_active"]:
            print('previous path:',project_path)

        if parameters["project"]["create_timestamp_folder"]:
            project_path = project_path + '/' + current_timestamp

            try:
                os.mkdir(project_path)
                if parameters["debug"]["is_active"]:
                    print("Folder %s created!" % project_path)
            except FileExistsError:
                if parameters["debug"]["is_active"]:
                    print("Folder %s already exists" % project_path)

    except Exception as e:
        print("An error occurred -- create timestamp folder:", str(e))

    # ---------------------------------
    # store general project variables: final project path to use
    # ---------------------------------

    project["general"]["project_path"] = project_path

    # ---------------------------------
    # 01_txt_to_json
    # ---------------------------------

    project["txt_to_json"]["input_file"] = parameters["module"]["01_txt_to_json"]["input_file"]

    if parameters["module"]["01_txt_to_json"]["output_file"] == "DEFAULT":
        project["txt_to_json"]["output_file"] = project_path + '/' + parameters["module"]["01_txt_to_json"]["default_folder"] + '/' + parameters["module"]["01_txt_to_json"]["default_file"]
    else:
        project["txt_to_json"]["output_file"] = parameters["module"]["01_txt_to_json"]["output_file"]

    try:
        os.mkdir(os.path.dirname(project["txt_to_json"]["output_file"]))
        if parameters["debug"]["is_active"]:
            print("Folder %s created!" % project["txt_to_json"]["output_file"])
    except FileExistsError:
        if parameters["debug"]["is_active"]:
            print("Folder %s already exists" % project["txt_to_json"]["output_file"])

    # --------------------------------
    # 02_replace
    # ---------------------------------

    if parameters["module"]["02_replace"]["input_file"] == "DEFAULT":
        project["replace"]["input_file"] = project["txt_to_json"]["output_file"]
    else:
        project["replace"]["input_file"] = parameters["module"]["02_replace"]["input_file"]

    if parameters["module"]["02_replace"]["output_file"] == "DEFAULT":
        project["replace"]["output_file"] = project_path + '/' + parameters["module"]["02_replace"]["default_folder"] + '/' + parameters["module"]["02_replace"]["default_file"]
    else:
        project["replace"]["output_file"] = parameters["module"]["02_replace"]["output_file"]

    try:
        os.mkdir(os.path.dirname(project["replace"]["output_file"]))
        if parameters["debug"]["is_active"]:
            print("Folder %s created!" % project["replace"]["output_file"])
    except FileExistsError:
        if parameters["debug"]["is_active"]:
            print("Folder %s already exists" % project["replace"]["output_file"])
    
    # --------------------------------
    # 03_replicate
    # ---------------------------------

    if parameters["module"]["03_replicate"]["input_file"] == "DEFAULT":
        project["replicate"]["input_file"] = project["replace"]["output_file"]
    else:
        project["replicate"]["input_file"] = parameters["module"]["03_replicate"]["input_file"]

    if parameters["module"]["03_replicate"]["output_file"] == "DEFAULT":
        project["replicate"]["output_file"] = project_path + '/' + parameters["module"]["03_replicate"]["default_folder"] + '/' + parameters["module"]["03_replicate"]["default_file"]
    else:
        project["replicate"]["output_file"] = parameters["module"]["03_replicate"]["output_file"]

    try:
        os.mkdir(os.path.dirname(project["replicate"]["output_file"]))
        if parameters["debug"]["is_active"]:
            print("Folder %s created!" % project["replicate"]["output_file"])
    except FileExistsError:
        if parameters["debug"]["is_active"]:
            print("Folder %s already exists" % project["replicate"]["output_file"])

    # --------------------------------
    # 04_probability
    # ---------------------------------

    if parameters["module"]["04_probability"]["input_file"] == "DEFAULT":
        project["probability"]["input_file"] = project["replicate"]["output_file"]
    else:
        project["probability"]["input_file"] = parameters["module"]["04_probability"]["input_file"]

    if parameters["module"]["04_probability"]["output_file"] == "DEFAULT":
        project["probability"]["output_file"] = project_path + '/' + parameters["module"]["04_probability"]["default_folder"] + '/' + parameters["module"]["04_probability"]["default_file"]
    else:
        project["probability"]["output_file"] = parameters["module"]["04_probability"]["output_file"]

    try:
        os.mkdir(os.path.dirname(project["probability"]["output_file"]))
        if parameters["debug"]["is_active"]:
            print("Folder %s created!" % project["probability"]["output_file"])
    except FileExistsError:
        if parameters["debug"]["is_active"]:
            print("Folder %s already exists" % project["probability"]["output_file"])

    # --------------------------------
    # 05_generate
    # ---------------------------------

    if parameters["module"]["05_generate"]["input_file"] == "DEFAULT":
        project["generate"]["input_file"] = project["probability"]["output_file"]
    else:
        project["generate"]["input_file"] = parameters["module"]["05_generate"]["input_file"]

    if parameters["module"]["05_generate"]["output_file"] == "DEFAULT":
        project["generate"]["output_file"] = project_path + '/' + parameters["module"]["05_generate"]["default_folder"] + '/' + parameters["module"]["05_generate"]["default_file"]
    else:
        project["generate"]["output_file"] = parameters["module"]["05_generate"]["output_file"]

    try:
        os.mkdir(os.path.dirname(project["generate"]["output_file"]))
        if parameters["debug"]["is_active"]:
            print("Folder %s created!" % project["generate"]["output_file"])
    except FileExistsError:
        if parameters["debug"]["is_active"]:
            print("Folder %s already exists" % project["generate"]["output_file"])

    # --------------------------------
    # show general project variables
    # ---------------------------------

    if parameters["debug"]["is_active"]:
        print("return len:",len(project))

    # -------------------------------

    return project

# ------------------------
# 01_txt_to_json
# ------------------------

def process_txt_to_json(file_path, is_mode_debugging = False):
    """
    Convert a text file with indentation to a nested JSON structure.
    This script is useful for converting structured text files into a hierarchical JSON format.
    If the label is between { }, it is considered as a replace candidate and isreplacecandidate 
    is set to True, otherwise False. If a value is present, it is converted to an integer and 
    isprobability is set to True, otherwise False. If the node is in the first level hierarchy, 
    isoriginal is set to True, otherwise False.

    Features implemented:
    - 2023-09-30: Extend the parsing from 1 comma separated value to 3 comma separated values. 
      The first parameter is 'value'. the second parameter is 'generatemin' and the third is 
      'generatemax'. set 'isreplicated' = true. in case of missing values replace value with -1 
      and set 'isreplicated' = false and 'isreplicatecandidate' = true.
    - 2023-10-17: Comment out sections in TXT using $ character and ignoring blank lines in TXT.

    Parameters:
    - file_path (str): This is the path to the input text file that needs to be converted into 
    a JSON structure.
    - debugmode (boolean)
    - output_filename (str)

    Returns:
    The function returns a dictionary which represents the root of the resulting JSON 
    structure. If an error occurs during the processing of the file, the function will 
    print an error message and return None.
    """

    if is_mode_debugging:
        print("--- MODULE: txt_to_json ---")

    try:
        # Initialize the root of the JSON structure and a dictionary to keep track of the current node at each indentation level
        root = []
        levels = {0: root}

        # Open the input file
        with open(file_path, 'r') as f:
            # Process each line in the file
            for line in f:

                # Filter out comment lines and empty rows in TXT
                if (len(line.strip()) > 0 and line.strip()[:1] != '$'):

                    # Determine the indentation level of the current line
                    indent = len(line) - len(line.lstrip())

                    # Split the line into a label and a value (if present)
                    parts = line.strip().split(',')
                    
                    label = parts[0]

                    value = int(parts[1]) if len(parts) > 1 and parts[1] else -1
                    generatemin = int(parts[2]) if len(parts) > 2 and parts[2] else -1
                    generatemax = int(parts[3]) if len(parts) > 3 and parts[3] else -1

                    # DEBUGGING
                    if is_mode_debugging:
                        print(indent, label, value, generatemin, generatemax)

                    # Create a new node with the label and value
                    node = {'description': label}

                    # type: replacement
                    if '{' in label or '}' in label:
                        node['description'] = label.replace('{', '').replace('}', '')
                        node['isreplacecandidate'] = True
                        node['isreplaced'] = False
                    else:
                        node['isreplacecandidate'] = False
                        node['isreplaced'] = False

                    # type: probability value
                    node['value'] = value

                    if value != -1:
                        node['isprobability'] = True
                    else:
                        node['isprobability'] = False

                    # type: generate replications
                    node['generatemin'] = generatemin
                    node['generatemax'] = generatemax

                    node['isreplicated'] = False
                    node['clonenr'] = 1

                    if generatemin != -1 and generatemax != -1:
                        node['isreplicatecandidate'] = True
                        node['isreplicated'] = False
                    else:
                        node['isreplicatecandidate'] = False
                        node['isreplicated'] = False

                    # Add 'original' = True if node is in first level hierarchy
                    if indent == 0:
                        node['isoriginal'] = True
                    else:
                        node['isoriginal'] = False

                    # Add the new node to the current level in the JSON structure
                    levels[indent].append(node)

                    # Update the current node at this indentation level and all higher levels
                    levels[indent + 4] = node.setdefault('children', [])

                else:
                    # DEBUGGING
                    if is_mode_debugging:
                        print('skip comment or empty line:', '"' + line + '"')

        # Remove empty 'children' nodes
        def remove_empty_children(node):
            if 'children' in node and not node['children']:
                del node['children']
            else:
                for child in node.get('children', []):
                    remove_empty_children(child)

        for node in root:
            remove_empty_children(node)

        return root

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# ---------------------------------------
# 02_replace
# ---------------------------------------

def find_and_replace(node, original_nodes):
    if node['isreplacecandidate'] and not node['isreplaced']:
        for original_node in original_nodes:
            if original_node['description'] == node['description']:
                node['children'] = original_node['children']
                node['isreplaced'] = True
    for child in node.get('children', []):
        find_and_replace(child, original_nodes)

def process_replace(input_file, output_file, is_mode_debugging = False):
    """
    Read JSON file, then iterates over the data to find and replace nodes based 
    on the specified conditions. It handles multiple levels of nesting, keeps the 
    'value' and 'isreplacecandidate' fields in the replaced candidate and updates the 
    'isreplaced' field to True. It deletes the 'isoriginal' field in the replaced node.
    This function is useful for manipulating hierarchical JSON data, particularly 
    to replace certain nodes based on specific criteria. The function is a recursive 
    function that operates on a node of a JSON structure.

    NEXT STEPS:
    - count iterations and stop infinite replications

    (A) IMPORTANT: The replace candidate in curly brackets has to be the highest indent node.

    (A.1) This example will work:

        [rel_key_I]
            {static_harmony}
        cadence

    (A.2) This example will work:

        [rel_key_I]
            {static_harmony}
            cadence

    (A.3) This example will NOT work:

        [rel_key_I]
            {static_harmony}
                cadence

    Parameters:
    node (dict): This is a dictionary representing a node in the JSON structure. Each 
    node is expected to have the following keys: 'description', 'isreplacecandidate', 
    'isreplaced', and optionally 'children' if the node has child nodes.

    Returns:
    The function does not explicitly return a value. Instead, it modifies the input 
    JSON structure in-place. Specifically, it iterates over the data to find and replace 
    nodes based on the specified conditions. If a node is marked as a replace candidate 
    and has not been replaced yet, it replaces the 'children' of the node with those of 
    the original node with the same 'description', and updates the 'isreplaced' field 
    to True.
    """
    if is_mode_debugging:
        print("--- MODULE: replace ---")

    with open(input_file, 'r') as f:
        data = json.load(f)

    original_nodes = [node for node in data if node['isoriginal']]

    for node in data:
        find_and_replace(node, original_nodes)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# --------------------------
# 03_replicate
# --------------------------

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
                #new_node['description'] = new_node['description'] + '(' + str(i + 1) + ')'

                # Insert the duplicate node at the same indent level as the original
                parent.insert(key + i + 1, new_node)

        for k, v in list(node.items()):  # Convert to list to avoid RuntimeError
            recursive_search(v, node, k)

    elif isinstance(node, list):
        i = 0
        while i < len(node):  # Use while loop to manually control the index
            recursive_search(node[i], node, i)
            i += 1

def process_replicate(input_file, output_file, is_mode_debugging = False):
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
                    item,,2,8
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

            ["song"["placeholder_a"["item_a"["placeholder_b"["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]]]["item_a"["placeholder_b"["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]["item_b"["note"]]]]]]

        (A) IMPORTANT:

        (A.1) This example will NOT work:

            static
                none,10
                I,10,1,8

        (A.2) This example will work instead:

            static
                none,10
                item,10
                    I,,1,8
    """
    if is_mode_debugging:
        print("--- MODULE: replicate ---")

    with open(input_file, 'r') as f:
        data = json.load(f)

    recursive_search(data)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# ---------------------------------------
# 04_probability
# ---------------------------------------

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

def process_probability(input_file, output_file, is_mode_debugging = False):
    if is_mode_debugging:
        print("--- MODULE: probability ---")

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

# ---------------------------------------
# class section
# ---------------------------------------

class File_management:
    pass

class Text_to_json:
    pass