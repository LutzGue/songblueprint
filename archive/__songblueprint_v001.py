def parse_file(filename):
    data = {}
    stack = [data]
    keys_count = {}
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            indent_level = len(line) - len(stripped_line.lstrip(' '))
            stack = stack[:indent_level+1]
            if ',' in stripped_line:
                key, value = stripped_line.split(',')
                if value.strip().isdigit():
                    stack[-1][key] = {'value': value.strip()}
                else:
                    stack[-1][key] = value.strip()
            else:
                new_dict = {}
                key = stripped_line
                keys_count[key] = keys_count.get(key, 0) + 1
                key += str(keys_count[key])
                stack[-1][key] = new_dict
                stack.append(new_dict)
    return data

indent = 0
def format_dict(d):
    global indent
    res = ""
    for key in d:
        res += ("   " * indent) + key + ":\n"
        if not type(d[key]) == type({}):
            res += ("   " * (indent + 1)) + d[key] + "\n"
        else:
            indent += 1
            res += format_dict(d[key])
            indent -= 1
    return res

#test

filename = 'txt\\phrase1.txt'
data = parse_file(filename)
print(data)

print(format_dict(data))