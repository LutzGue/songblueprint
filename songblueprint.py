import os
import datetime
import logging
import json
import metalanguage

# Define the parameters for the project and manage excecution modules
parameters = {
    "project": {
        
        # general path in which generated json files are stored into.
        # default value "./json"
        "project_path": "./json",

        # True: (recommended) creates new folder named by project name.
        # False: no seperate project folder in use. will store all files into ./json/ folder without grouping them.
        "create_project_folder": True,

        # "DEFAULT": (recommended) automatically --> get project title from txt_to_json filetitle
        # "<my_title>"": individual --> e.g. "modulation_test" / "modulation_productive"
        "project_name": "DEFAULT",

        # True: structured folders grouped by: year/month/day
        # False: withour grouped folders creation
        "create_date_folder": True,

        # True: create separate folder using timestamp
        # False: without separate folder creation
        "create_timestamp_folder": True,

        "excecution_mode": "INDIVIDUAL" # ALL, INDIVIDUAL, PRE, POST
    },
    "log": {
        "is_active": True,
        "is_store_file": True,
        "is_timestamp": True,
        "is_show_console": True,
        "path": "./log/",
        "file_title": "protocol.log"
    },
    "debug": {

        # True: enable console to debug (e.g. path creation variables, timestamp, ...)
        # False: disable console messages
        "is_active": True
    },
    "module": {
        "01_txt_to_json": {

            # path and filename to TXT file to parse and convert to JSON
            # e.g.: "./txt/experimental/modulation1.txt"
            "input_file": "./txt/experimental/vanilla1.txt",

            # "DEFAULT": <current project folder>/"output-txt_to_json.json"
            # "my file": user defined folder, e.g.: "./tmp/output_tmp1.json"
            "output_file": "DEFAULT",

            # default: "txt_to_json"
            "default_folder": "01_txt_to_json",

            # default: "output-txt_to_json.json"
            "default_file": "output-txt_to_json.json",

            # TRUE: excecut e new generation of data
            # FALSE: skip generation and use specific folder
            "is_excecute": True,

            "is_store_file": True
        },
        "02_replace": {

            # "DEFAULT": picks automatically the previously created "output-txt_to_json.json"-file in the same project- and timestamp folder
            # "my file": you can change to the specivic path if you want to use archived "output-txt_to_json.json"-files, e.g. ".\json\modulation1\2023\10\25\2023_10_25T17_26_10\output-txt_to_json.json" and save computation time.
            "input_file": "DEFAULT",

            # "DEFAULT": "output-replace.json
            # "my file": user defined folder, e.g.: "./tmp/output_tmp1.json"
            "output_file": "DEFAULT",

            # default: "replace"
            "default_folder": "02_replace",

            # default: "output-replace.json"
            "default_file": "output-replace.json",

            # TRUE: excecut e new generation of data
            # FALSE: skip generation and use specific folder
            "is_excecute": True,

            "is_store_file": True,
        },
        "03_replicate": {

            # "DEFAULT"
            # <my file>
            "input_file": "DEFAULT",

            # "DEFAULT"
            # <my file>
            "output_file": "DEFAULT",

            # default: "replicate"
            "default_folder": "03_replicate",

            # default: "output-replicate.json", the id e.g. "-001" will be added automatically
            "default_file": "output-replicate.json",

            # TRUE: excecut e new generation of data
            # FALSE: skip generation and use specific folder
            "is_excecute": True,

            "is_store_file": True,

            # number of files to generate (e.g.: 10)
            "generate_count": 2
        },
        "04_probability": {
            "input_file": "DEFAULT",
            "output_file": "DEFAULT",

            # default: ""
            "default_folder": "04_probability",

            # default: ""
            "default_file": "output-probability.json",

            "is_excecute": True,
            "is_store_file": True,
        },
        "05_generate": {
            "input_file": "DEFAULT",
            "output_file": "DEFAULT",

            # default: ""
            "default_folder": "05_generate",

            # default: "output-generate.json"
            "default_file": "output-generate.json",

            "is_excecute": True,
            "is_store_file": True,

            # default: 1 or 2 ( = n * m )
            "cartesian_count": 2
        },
    }
}

# --------------------------------
# 00_file management
# --------------------------------

# global variables
project = ""    # init

# excecute folder creation
project = metalanguage.file_management(parameters)

if parameters["debug"]["is_active"]:
    print("project:",project)

# -------------------------------
# 01_txt_to_json
# -------------------------------

# generate new
if parameters["module"]["01_txt_to_json"]["is_excecute"]:

    # (1) converting txt to json
    json_data = metalanguage.process_txt_to_json(project["txt_to_json"]["input_file"], parameters["debug"]["is_active"])

    if parameters["debug"]["is_active"]:
        print("json_data LEN:",len(json_data))

    # store json file
    if json_data is not None:
        with open(project["txt_to_json"]["output_file"], 'w') as f:
            json.dump(json_data, f, indent=4)

    if parameters["debug"]["is_active"]:
        print("output_file:",project["txt_to_json"]["output_file"], os.path.getsize(project["txt_to_json"]["output_file"]))

# ------------------------
# 02_replace
# ------------------------

# generate new
if parameters["module"]["02_replace"]["is_excecute"]:
    json_data = metalanguage.process_replace(project["replace"]["input_file"],project["replace"]["output_file"], parameters["debug"]["is_active"])

if parameters["debug"]["is_active"]:
    print("output_file:",project["replace"]["output_file"], os.path.getsize(project["replace"]["output_file"]))


# ------------------------
# 03_replicate
# ------------------------

# generate new
if parameters["module"]["03_replicate"]["is_excecute"]:

    # Call the function with your input and output file paths. generate different schemas.
    for n in range(parameters["module"]["03_replicate"]["generate_count"]):
        output_filename_number = os.path.splitext(project["replicate"]["output_file"])[0] + '-' + str(n+1) + os.path.splitext(project["replicate"]["output_file"])[1]
        metalanguage.process_replicate(project["replicate"]["input_file"], output_filename_number, parameters["debug"]["is_active"])

        if parameters["debug"]["is_active"]:
            print("output_file:",output_filename_number, os.path.getsize(output_filename_number))

# --------------------------------
# 04_probability
# --------------------------------

# TODO: calculate for all n x generated "replicate" files n x new "probability" files:
#       --> n: range(parameters["module"]["03_replicate"]["generate_count"])

# generate new
if parameters["module"]["04_probability"]["is_excecute"]:

    # Call the function with your input and output file paths. generate different schemas.
    for n in range(parameters["module"]["03_replicate"]["generate_count"]):
        input_filename_number = os.path.splitext(project["probability"]["input_file"])[0] + '-' + str(n+1) + os.path.splitext(project["probability"]["input_file"])[1]
        output_filename_number = os.path.splitext(project["probability"]["output_file"])[0] + '-' + str(n+1) + os.path.splitext(project["probability"]["output_file"])[1]
        metalanguage.process_probability(input_filename_number, output_filename_number, parameters["debug"]["is_active"])

        if parameters["debug"]["is_active"]:
            print("output_file:",output_filename_number, os.path.getsize(output_filename_number))

# --------------------------------
# 05_generate
# --------------------------------

# TODO: calculate for randomly choosen "probability" files new "generate" file(s):
#       --> repeat random process user defined m-times (e.g. 1, 2, 10, 20, 100, 1000, ...)

# generate new
if parameters["module"]["05_generate"]["is_excecute"]:

    # Call the function with your input and output file paths. generate different schemas.
    for n in range(parameters["module"]["03_replicate"]["generate_count"]):
        for m in range(parameters["module"]["05_generate"]["cartesian_count"]):
            input_filename_number = os.path.splitext(project["probability"]["input_file"])[0] + '-' + str(n+1) + os.path.splitext(project["probability"]["input_file"])[1]
            output_filename_number = os.path.splitext(project["generate"]["output_file"])[0] + '-' + str(n+1) + '-' + str(m+1) + os.path.splitext(project["generate"]["output_file"])[1]
            metalanguage.process_probability(input_filename_number, output_filename_number, parameters["debug"]["is_active"])

            if parameters["debug"]["is_active"]:
                print("output_file:",output_filename_number, os.path.getsize(output_filename_number))

# --------------------------------
# parsetree
# --------------------------------


