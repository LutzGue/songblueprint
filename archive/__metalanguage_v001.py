import json
import os
import datetime
import logging

def file_management(parameters):

    # initial global variables
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

    # --------------------------------
    # 03_replicate
    # ---------------------------------

    if parameters["module"]["03_replicate"]["input_file"] == "DEFAULT":
        project["replicate"]["input_file"] = project["replace"]["output_file"]
    else:
        project["replicate"]["input_file"] = parameters["module"]["03_replicate"]["input_file"]


    # !!! FOR ... LOOP

    if parameters["module"]["03_replicate"]["output_file"] == "DEFAULT":
        project["replicate"]["output_file"] = project_path + '/' + parameters["module"]["03_replicate"]["default_folder"] + '/' + parameters["module"]["03_replicate"]["default_file"]
    else:
        project["replicate"]["output_file"] = parameters["module"]["03_replicate"]["output_file"]

    # --------------------------------
    # show general project variables
    # ---------------------------------

    if parameters["debug"]["is_active"]:
        print(project)

    # -------------------------------

def text_to_json(file_path, is_mode_debugging = False):
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
    - 2023-10-17: Comment out sections in TXT using # character and ignoring blank lines in TXT.

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
    try:
        # Initialize the root of the JSON structure and a dictionary to keep track of the current node at each indentation level
        root = []
        levels = {0: root}

        # Open the input file
        with open(file_path, 'r') as f:
            # Process each line in the file
            for line in f:

                # Filter out comment lines and empty rows in TXT
                if (len(line.strip()) > 0 and line.strip()[:1] != '#'):

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

# class section
class Text_to_json:
    pass