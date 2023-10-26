import os
import datetime
import logging
import json
import metalanguage

# Define the parameters for the project
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
            "default_folder": "txt_to_json",

            # default: "output-txt_to_json.json"
            "default_file": "output-txt_to_json.json",

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
            "default_folder": "replace",

            # default: "output-replace.json"
            "default_file": "output-replace.json",

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
            "default_folder": "replicate",

            # default: "output-replicate.json", the id e.g. "-001" will be added automatically
            "default_file": "output-replicate.json",

            "is_excecute": True,
            "is_store_file": True,
            "count": 10
        },
        "04_probability": {
            "input_file": "DEFAULT",
            "output_file": "DEFAULT",

            # default: ""
            "default_folder": "probability",

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
            "default_folder": "generate",

            # default: "output-generate.json"
            "default_file": "",

            "is_excecute": True,
            "is_store_file": True,
            "count": "DEFAULT"
        },
    }
}

# global variables
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

# Logfile
# LOG_FILE = "./log/" + dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d %H_%M_%S') + ".log"

# -------------------------------

# 01_txt_to_json

input_file = parameters["module"]["01_txt_to_json"]["input_file"]
output_file = parameters["module"]["01_txt_to_json"]["output_file"]

if output_file == 'DEFAULT':
    output_file = "./json/project/output.txt"

print(input_file, output_file)

# edit user defined parameters here
project_title = 'modulation1'
input_sub_path = 'experimental\\'

# generate new or use existing instead
excecute01 = True # "01_txt_to_json"
use_existingfor_01 = "dummy1"
excecute02 = False # "02_replicate"
use_existingfor_02 = "dummy1"
excecute03 = True # "03_replace"
use_existingfor_03 = "dummy1"
excecute04 = True # "04_probability"
use_existingfor_04 = "dummy1"
excecute05 = True # "05_generate"
use_existingfor_05 = "dummy1"
excecute06 = True # "06_roman_to_chords"
use_existingfor_06 = "dummy1"

use_project_folder = True
use_project_yearmonthday = True
use_timestamp_in_project_folder = True
folder01 = "01_txt_to_json"
folder02 = "02_replicate"
folder03 = "03_replace"
folder04 = "04_probability"
folder05 = "05_generate"
folder06 = "06_roman_to_chords"

store_data_in_file = True
store_data_in_memory = True
create_log = True

# timestamp
ft = "%Y_%m_%dT%H_%M_%S"
current_timestamp = datetime.datetime.now().strftime(ft)
current_year = datetime.datetime.now().strftime("%Y")
current_month = datetime.datetime.now().strftime("%m")
current_day = datetime.datetime.now().strftime("%d")
print('tmsp:',current_timestamp)

# create new folder for generated json files
if use_project_folder:
    path_to_project = './json/' + project_title

    try:
        os.mkdir(path_to_project)
        print("Folder %s created!" % path_to_project)
    except FileExistsError:
        print("Folder %s already exists" % path_to_project)
else:
    path_to_project = './json/'

if use_project_yearmonthday:
    path_to_year = path_to_project + '/' + current_year
    path_to_month = path_to_year + '/' + current_month
    path_to_day = path_to_month + '/' + current_day

    try:
        os.mkdir(path_to_year)
        print("Folder %s created!" % path_to_year)
    except FileExistsError:
        print("Folder %s already exists" % path_to_year)

    try:
        os.mkdir(path_to_month)
        print("Folder %s created!" % path_to_month)
    except FileExistsError:
        print("Folder %s already exists" % path_to_month)

    try:
        os.mkdir(path_to_day)
        print("Folder %s created!" % path_to_day)
    except FileExistsError:
        print("Folder %s already exists" % path_to_day)
else:
    path_to_day = path_to_project

if use_timestamp_in_project_folder:
    path_to_timestamp = path_to_day + '/' + current_timestamp
    try:
        os.mkdir(path_to_timestamp)
        print("Folder %s created!" % path_to_timestamp)
    except FileExistsError:
        print("Folder %s already exists" % path_to_timestamp)
else:
    path_to_timestamp = path_to_day

current_path = path_to_timestamp

print('path:',current_path)

# logger.debug ("Test")

# -----------------

# 01_txt_to_json

input_filename = 'txt\\' + input_sub_path + project_title + '.txt'
output_filename = 'json\\output.json'
#output_filename = 'json\\' + project_title + '\\output.json'

# generate new
if parameters["excecution"]["txt_to_json"]["enabled"]:

    # (1) converting txt to json
    json_data = metalanguage.text_to_json(input_filename, False)

    # store json file
    if json_data is not None:
        with open(output_filename, 'w') as f:
            json.dump(json_data, f, indent=4)

# (3) replace **


# (2) replicate **

if excecute02:

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


