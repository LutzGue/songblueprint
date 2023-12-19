"""
Dieses Skript definiert eine einfache Grammatik basierend auf Regeln und erzeugt dann einen Song in Form eines Parse Trees. Wahrscheinlichkeiten sind nach dem komma angegeben (z.B.: ,10). So lange den vorgang des Ersetzens wiederholen bis keine geschweiften klammern übrig sind oder ein maximum wert der vorgegebenen iterationen erreicht wurde (z.B. 100)

rules = {
    "SONG": ["{key}", "{I}", "{I}"],
    "I": [
        (["{I}", "{I}"], 10),
        (["{V}", "{I}"], 10),
        ([], 10)
    ],
    "V": [
        (["{ii}", "{V}"], 10),
        (["V/V", "{V}"], 10),
        ([], 10)
    ],
    "ii": [
        (["{vi}", "{ii}"], 10),
        ([], 10)
    ],
    "vi": [
        (["V/vi", "{vi}"], 10),
        ([], 10)
    ],
    "key": ["Ab", "Eb", "Bb", "F", "C", "G", "D", "A"]
}
Ausgabe im parse tree format:
beispiel:
[I_key=D[I C][I[V[ii Dm][V G]][I C]]]
"""

import random

def generate_song(grammar, max_iterations=100):
    start_symbol = "SONG"
    song = [start_symbol]

    for _ in range(max_iterations):
        new_song = []
        for symbol in song:
            if symbol in grammar:
                expansion = choose_expansion(grammar[symbol])
                if expansion is not None:
                    new_song.extend(expansion)
            else:
                new_song.append(symbol)
        song = new_song

        if all(isinstance(s, str) for s in song):
            break

    return "".join(song)

def choose_expansion(options):
    valid_options = []
    for option in options:
        if isinstance(option, (list, tuple)):
            valid_options.append(option)
        elif isinstance(option, str):
            valid_options.append((option, 1.0))

    if valid_options:
        total_weight = sum(option[1] for option in valid_options)
        rand_num = random.uniform(0, total_weight)
        cumulative_weight = 0
        for option in valid_options:
            cumulative_weight += option[1]
            if rand_num < cumulative_weight:
                return option[0]

    return None

# Definiere die Grammatikregeln
rules = {
    "SONG": ["{key}", "{I}", "{I}"],
    "I": [
        (["{I}", "{I}"], 10.0),
        (["{V}", "{I}"], 10.0),
        ([], 10.0)
    ],
    "V": [
        (["{ii}", "{V}"], 10.0),
        (["V/V", "{V}"], 10.0),
        ([], 10.0)
    ],
    "ii": [
        (["{vi}", "{ii}"], 10.0),
        ([], 10.0)
    ],
    "vi": [
        (["V/vi", "{vi}"], 10.0),
        ([], 10.0)
    ],
    "key": ["Ab", "Eb", "Bb", "F", "C", "G", "D", "A"]
}

# Generiere den Song im Parse-Tree-Format
generated_song = generate_song(rules)
print(f"Beispiel: {generated_song}")
