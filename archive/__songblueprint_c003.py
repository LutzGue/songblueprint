import os
import datetime
import logging
import json
import metalanguage

# Logfile
# LOG_FILE = "./log/" + dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d %H_%M_%S') + ".log"

parameters = {
    "logging": {
        "description": "status success and error messages will be protocolled in log file using timestamps. startingpoint for debugging process.",
        "enabled": True,
        "console_print": True,
        "output_file": {
            "store_log_file": True,
            "path": "./log/",
            "title": "protocol",
            "extension": "log",
            "use_timestamp": True
        }
    },
    "project": {
        "description": "input file to parse.",
        "input_file": {
            "path": "./txt/experimental/",
            "title": "dynamic1",
            "extension": "txt"
        }
    },
    "general_project_folder": {
        "description": "path to save generated data inthe hierarchical schema: <PROJECT>/<YEAR>/<MONTH>/<DAY>/<TIMESTAMP>/<filetitle>.json",
        "main_path": "./json/",
        "project": {
            "create_folder": True,
            "use_project_title": True,
            "different_title": ""
        },
        "date": {
            "create_folder": True,
        },
        "timestamp":{
            "create_folder": True,
        }
    },
    "excecution": {
        "description": "settings for the different generation modules.",
        "txt_to_json": {
            "enabled": True,
            "genrate_new": True,
            "input_file":{
                "use_default": True,
                "different_file_name": ""
            },
            "output_file":{
                "store_data_in_file": True,
                "store_data_in_memory": True,
                "create_sub_folder": "01_txt_to_json",
            },
            "debug_console_print": True,
            "generate_parsetree": False
        },
        "replicate":{
            "enabled": True,
            "genrate_new": True,
            "input_file":{
                "description": "default file is the generated file in txt_to_json module. in case you have deactivated execution of txt_to_json you can use archived json data instead. just reference to the specific folder.",
                "use_default": True,
                "different_file_name": ""
            },
            "output_file":{
                "store_data_in_file": True,
                "store_data_in_memory": True,
                "create_sub_folder": "01_txt_to_json",
            },
            "debug_console_print": True,
            "generate_parsetree": False
        },
        "replace":{
        },
        "generate":{
        },
        "roman_to_chords":{
        }
    }
}
print(parameters["excecution"]["txt_to_json"])

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


