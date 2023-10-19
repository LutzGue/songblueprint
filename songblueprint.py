import json
import metalanguage

# edit user defined parameters here
input_filename = 'txt\\reharmonization2.txt'
output_filename = 'json\\output.json'
store_data_in_memory = True
store_data_in_file = True
create_log = True

# (1) converting txt to json
json_data = metalanguage.text_to_json(input_filename, False)

# store json file
if json_data is not None:
    with open(output_filename, 'w') as f:
        json.dump(json_data, f, indent=4)

# (2) replicate

# edit user defined parameters here
# input_filename = 'json\\output.json'
output_filename_syntax = 'json\\output_replicate-'
generate_count = 10

# Call the function with your input and output file paths. generate different schemas.
for n in range(generate_count):
   output_filename_number = output_filename_syntax + str(n+1) + '.json'
   metalanguage.process_json_file(input_filename, output_filename_number)

# (3) replace

# (probability)

# (4) generate

# parsetree

