"""
- gegeben sei folgender parsetree als beispiel:
# Eingabe:
    [A[B[D x1]][C[E[G x2][H[I x3]]][F x4]]]
- zu jedem element x soll der entsprechende weg aufgezeigt werden.
- in dem beispiel parsetree ist die ausgabe folgende:
# Ausgabe:
    element;weg
    x1;(A -> B -> D)
    x2;(A -> C -> E -> G)
    x3;(A -> C -> E -> H -> I)
    x4;(A -> C -> F)
# Beispiel Parsetree als String
#parsetree_str = "[AAA[BBBBBB[DD xyz1]][CCC[E[G xx2][HH[I x3]]][FFFFFF xxxxx4]]]"
#parsetree_str = "[S:KEY_F[P:KEY_I[PROL[PRE:V[V35|V35 x ][V56|V56 x ]][TON:I[I|i[sub[iii|? x ]]]]][CAD[CAD:V[V7|V7 x ]]]]]"
#parsetree_str = "[S:KEY_e[P:KEY_I[PROL[TON:I[I|i[I46|i46 x ]][(V|V)[V35|V35 x ]][I|i[sub[IV6|? x ]]]]][conn[V35/--> x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[vi|? x]]]]]"
#parsetree_str = "[S:KEY_d[P:KEY_I[PROL[PRE:V[V56|V56 x ]][TON:I[I|i[SOP[I|i [I46|i46 x =y:MOD_?]][ii|? [ii2|? x]][V|? [V56|V56 x ]][I|i [I46|i46 x =y:MOD_?]]]]]][conn[ii35|? x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[PLAG-TAG[IV|? x][IV|? x][I|i x]]]]]]"

# Beispiel:
['SKEYe', ['PKEYI', ['PROL', ['TONI', ['Ii', ['Ii ', 'x ']], ['VV', ['VV ', 'x ']], ['Ii', ['sub', ['IV ', 'x ']]]]], ['conn', ['V ', 'x']], ['CAD', ['CADV', ['CADV', ['VV ', 'x'], ['VV ', 'x']]], ['CADI', ['vi ', 'x']]]]]
element;weg
x ;(SKEYe -> PKEYI -> PROL -> TONI -> VV -> VV )
x ;(SKEYe -> PKEYI -> PROL -> TONI -> Ii -> sub -> IV )
x;(SKEYe -> PKEYI -> conn -> V )
x;(SKEYe -> PKEYI -> CAD -> CADV -> CADV -> VV )
x;(SKEYe -> PKEYI -> CAD -> CADV -> CADV -> VV )
x;(SKEYe -> PKEYI -> CAD -> CADI -> vi )

- basierend auf diesen pfaden können regeln abgeleitet werden:
    Regel 1) Tonart identifizieren.
    Regel 2) Moll oder Dur Tonart für I bzw. i auswählen.
    Regel 3) Mögliche Modulationstonarten basierend auf Pivotchords ermitteln.
    Regel 4) Aus abgeleiteter Tonart und Romannumeral den Akkordnamen mappen (10_pivot.py).
"""

def parse_tree(tree, root=None, path=None):
    if path is None:
        path = []
    if root is None:
        root = tree[0]

    for elem in tree[1:]:
        if isinstance(elem, list):
            parse_tree(elem, root, path + [elem[0]])
        else:
            path_with_root = [root] + path
            print(f'{elem};({" -> ".join(path_with_root)})')

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

#parsetree_str = "[AA:A[BBB|BBB[DD xyz1]][CCC[E[G xx2][HH[I x3]]][FFF__FFF xxxxx4]]]"
#parsetree_str = "[S:KEY_F[P:KEY_I[PROL[PRE:V[V35|V35 x ][V56|V56 x ]][TON:I[I|i[sub[iii|? x ]]]]][CAD[CAD:V[V7|V7 x ]]]]]"
#parsetree_str = "[S:KEY_e[P:KEY_I[PROL[TON:I[I|i[I46|i46 x ]][(V|V)[V35|V35 x ]][I|i[sub[IV6|? x ]]]]][conn[V35/--> x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[vi|? x]]]]]"
parsetree_str = "[S:KEY_d[P:KEY_I[PROL[PRE:V[V56|V56 x ]][TON:I[I|i[SOP[I|i [I46|i46 x:y:MOD_?]][ii|? [ii2|? x]][V|? [V56|V56 x ]][I|i [I46|i46 x:y:MOD_?]]]]]][conn[ii35|? x]][CAD[CAD:V[CAD_V64[V46|V46 x][V357|V357 x]]][CAD:I[PLAG-TAG[IV|? x][IV|? x][I|i x]]]]]]"

parsed_tree = parse_string(parsetree_str)

print(parsed_tree)

print('------------------------------------------')
parse_tree(parsed_tree)
print('------------------------------------------')