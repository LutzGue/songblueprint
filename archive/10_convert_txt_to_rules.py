def read_rules_file(file_path):
    """
    The function `read_rules_file` reads a text file containing specific rules and returns a dictionary that organizes these rules. Here are the details of the function and its parameters:

    - **Function:** `read_rules_file`

    - **Parameter:**
    - `file_path`: A string specifying the file path to the text file containing the rules.

    - **Function Description:**
    - The function reads the specified text file (`file_path`) line by line.
    - It ignores empty lines and lines starting with '$'. These lines are used for adding comments in the text.
    - Identifies the first level (e.g., "key") and creates an empty list for the rules of that key.
    - Identifies the second level (e.g., "{key_maj}, 12") and adds it to the list for the current key.
    - The resulting dictionary has keys representing the first level and values as lists of tuples. Each tuple represents the second level with a key and an associated value.

    - **Return Value:**
    - A dictionary reflecting the structure of the rules from the text file.
    
    - **Example Input:**
    ```
    $ Tonarten
    key
        {key_maj}, 12
        {key_min}, 10
        key_dorian, 3
    $ Dur-Tonart
    key_maj
        key_Bb{start_maj}, 5
        key_F{start_maj}, 5
        key_C{start_maj}, 5
    $ Moll-Tonart
    key_min
        key_g{start_min}, 5
        key_d{start_min}, 5
        key_a{start_min}, 5
    $ Weitere Regeln
    ```

    - ***Example Output:***
    ```
    {'key': [('{key_maj}', 12), ('{key_min}', 10), ('key_dorian', 3)], 'key_maj': [('key_Bb{start_maj}', 5), ('key_F{start_maj}', 5), ('key_C{start_maj}', 5)], 'key_min': [('key_g{start_min}', 5), ('key_d{start_min}', 5), ('key_a{start_min}', 5)]}         
    ```
    
    - **Example Call:**
    ```python
    file_path = 'rules.txt'
    rules = read_rules_file(file_path)
    print(rules)
    ```

    The function assumes that the text file follows specific formatting to recognize and extract the rules correctly. In this case, the rules are organized in a nested dictionary that reflects the hierarchical structure of keys and values.
    """
    rules = {}
    current_key = None

    with open(file_path, 'r') as file:
        for line in file:

            # Ignoriere leere Zeilen und Zeilen, die mit '$' beginnen
            if not line.strip() or line.strip().startswith('$'):
                continue

            # Identifiziere die erste Ebene (z.B. "key") und erstelle eine leere Liste
            if not line.startswith((' ', '\t')):
                current_key = line.strip()
                rules[current_key] = []
            else:
                # Identifiziere die zweite Ebene (z.B. "{key_maj}, 12") und füge sie zur Liste hinzu
                key, value = map(str.strip, line.split(','))
                rules[current_key].append((key, int(value)))

    return rules

# Beispielaufruf mit der Datei "rules.txt"
file_path = 'rules.txt'
rules = read_rules_file(file_path)

# Ausgabe des resultierenden Dictionaries
print(rules)