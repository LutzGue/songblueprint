def parse_tree(tree, stats=None):
    if stats is None:
        stats = {}

    for elem in tree:
        if isinstance(elem, list):
            parse_tree(elem, stats)
        else:
            normalized_elem = str(elem).strip()  # Normalisieren Sie die Zeichenkette hier
            stats[normalized_elem] = stats.get(normalized_elem, 0) + 1

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
                if current_list and current_list[-1] and isinstance(current_list[-1], str) and (not current_list[-1] or current_list[-1][-1].isalnum() or current_list[-1][-1] in special_char):  
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

#parsetree_str = "[AA:A[BBB|BBB[DD xyz1]][AA:A[E[AA:A xx2][AA:A[I x3]]][FFF__FFF xyz1]]]"#parsetree_str = "[AA:A[BBB|BBB[DD xyz1]][CCC[E[G xx2][HH[I x3]]][FFF__FFF xxxxx4]]]"
#parsetree_str = "[S:KEY_F[P:KEY_I[PROL[PRE:V[V35|V35 x ][V56|V56 x ]][TON:I[I|i[sub[iii|? x ]]]]][CAD[CAD:V[V7|V7 x ]]]]]"
#parsetree_str = "[S:KEY_e[P:KEY_I[PROL[TON:I[I|i[I46|i46 x ]][(V|V)[V35|V35 x ]][I|i[sub[IV6|? x ]]]]][conn[V35/--> x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[vi|? x]]]]]"
parsetree_str = "[S:KEY_d[P:KEY_I[PROL[PRE:V[V56|V56 x ]][TON:I[I|i[SOP[I|i [I46|i46 x:y:MOD_?]][ii|? [ii2|? x]][V|? [V56|V56 x ]][I|i [I46|i46 x:y:MOD_?]]]]]][conn[ii35|? x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[PLAG-TAG[IV|? x][IV|? x][I|i x]]]]]]"

parsed_tree = parse_string(parsetree_str)

stats = parse_tree(parsed_tree)

printed_keys = set()
for key, value in stats.items():
    if key not in printed_keys:
        print(f'{key} -> {value}')
        printed_keys.add(key)
