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
            "input_file": "./txt/experimental/modulation1.txt",

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
            "count": 10
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
            "count": "DEFAULT"
        },
        "05_generate": {
            "input_file": "DEFAULT",
            "output_file": "DEFAULT",

            # default: ""
            "default_folder": "05_generate",

            # default: "output-generate.json"
            "default_file": "",

            "is_excecute": True,
            "is_store_file": True,
            "count": "DEFAULT"
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
    json_data = metalanguage.text_to_json(project["txt_to_json"]["input_file"], parameters["debug"]["is_active"])

    if parameters["debug"]["is_active"]:
        print("json_data LEN:",len(json_data))

    # store json file
    if json_data is not None:
        with open(project["txt_to_json"]["output_file"], 'w') as f:
            json.dump(json_data, f, indent=4)

# ------------------------
# 02_replace
# ------------------------

# generate new
if parameters["module"]["02_replace"]["is_excecute"]:
    print("xx")

# ------------------------
# 03_replicate
# ------------------------

# generate new
if parameters["module"]["03_replicate"]["is_excecute"]:

    # edit user defined parameters here
    input_filename = 'json\\output.json'
    output_filename_syntax = 'json\\output_replicate-'
    generate_count = 10

    # Call the function with your input and output file paths. generate different schemas.
    for n in range(generate_count):
        output_filename_number = output_filename_syntax + str(n+1) + '.json'
        metalanguage.process_json_file(input_filename, output_filename_number)

# (probability)

# (4) generate

# parsetree


