def parse_tree(tree, stats=None):
    if stats is None:
        stats = {}

    for elem in tree:
        if isinstance(elem, list):
            parse_tree(elem, stats)
        else:
            stats[elem] = stats.get(elem, 0) + 1

    return stats

def parse_string(input_str):
    stack = [[]]
    current_list = stack[-1]

    special_char = '|:<=>/-_,\;.+#!"§$%&()?'

    i = 0
    while i < len(input_str):
        char = input_str[i]

        if char.isalnum() or char.isspace() or char in special_char:
            if char.isalnum() or char in special_char or (char.isspace() and current_list and current_list[-1] and isinstance(current_list[-1], str)):
                if current_list and current_list[-1] and isinstance(current_list[-1], str) and (not current_list[-1] or current_list[-1][-1].isalnum() or current_list[-1][-1] in special_char):  # Hier wurde die Bedingung geändert
                    current_list[-1] += char 
                else:
                    current_list.append(char) 
            elif char.isspace() and not current_list:
                current_list.append(char)
            else:
                current_list.append(char)
        elif char == '[':
            new_list = []
            current_list.append(new_list)
            stack.append(new_list)
            current_list = new_list
        elif char == ']':
            stack.pop()
            if stack:
                current_list = stack[-1]

        i += 1

    return stack[0][0]

parsetree_str = "[AA:A[BBB|BBB[DD xyz1]][CCC[E[AA:A xx2][HH[I x3]]][FFF__FFF xxxxx4]]]"

parsed_tree = parse_string(parsetree_str)

stats = parse_tree(parsed_tree)

for key, value in stats.items():
    print(f'{key} -> {value}')
