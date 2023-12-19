"""
### Beschreibung:
- es wird eine tonart vorgegeben. diese kann dur oder moll sein. Z.B. groß geschriebenes "G" für tonart "G-Dur", oder klein geschriebenes "f" für "F-Moll".
- es wird ein roman numeral vorgegeben. Z.B. großgeschriebenes "I" für Stufe 1 in der Dur-Tonart als Dur-Akkord, oder klein geschriebes "ii" für Stufe 2 in der Dur-Tonart als Moll-Akkord.
- zu dem vorgegebenen roman numeral in der vorgegeben tonart wird der akkord ermittelt. Z.B. in der Dur-Tonart "C" ist Roman Numeral "I" der Akkord "C", oder in der Dur-Tonart "C" ist Roman Numeral "ii" der Akkord "Dm".
- anschließend wird zu diesem ermittelten akkord eine liste möglicher tonarten (sowie in dur als auch moll) erstellt, in denen dieser akkord vorkommt. zusätzlich werden alle die roman numerale in den ermittelten tonarten zugewiesen.

### Beispiele:
Vorgegebene Tonart: G (G-Dur)
Vorgegebenes Roman Numeral: I
Ermittelter Akkord: G
Mögliche Tonarten mit diesem Akkord:
1: G-Dur (I)
2: D-Dur (V)

Vorgegebene Tonart: f (F-Moll)
Vorgegebenes Roman Numeral: ii
Ermittelter Akkord: Gm
Mögliche Tonarten mit diesem Akkord:
1: F-Moll (ii)
2: Bb-Dur (vi)

Vorgegebene Tonart: C (C-Dur)
Vorgegebenes Roman Numeral: IV
Ermittelter Akkord: F
Mögliche Tonarten mit diesem Akkord:
1: C-Dur (IV)
2: G-Dur (I)

Vorgegebene Tonart: d (d-Moll)
Vorgegebenes Roman Numeral: vi
Ermittelter Akkord: Bb
Mögliche Tonarten mit diesem Akkord:
1: d-Moll (vi)
2: G-Moll (iii)

### Schritt 1: gib den entsprechenden akkord zu der kombination von tonart und roman numeral aus.

### CODE:

# Mapping der Dur- und Moll-Akkorde für die Stufen I bis VII
dur_romannumerale = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
moll_romannumerale = ["i", "ii°", "III", "iv", "v", "VI", "VII"]

# Tonarten und deren zugehörige Akkorde
tonarten_akkorde = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "f": ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb", "Fdim"],
    "d": ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C", "Ddim"],
    "g": ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F", "Gdim"],
    "c": ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb", "Cdim"],
    "a": ["Am", "Bdim", "C", "Dm", "Em", "F", "G", "Adim"],
    "e": ["Em", "F#dim", "G", "Am", "Bm", "C", "D", "Edim"],
    "b": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A", "Bdim"],
    "f#": ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E", "Fdim"],
    "c#": ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B", "Cdim"],
}

# Beispiele: 
# Eingabe-Parameter: Kombination aus Tonart (Dur / Moll) und Romannumeral.
# Ausgabe-Parameter: Gemappter Akkordname.
print(ermittel_akkord("G", "I"))  # --> "G"
print(ermittel_akkord("f", "ii°"))  # --> "Gdim"
print(ermittel_akkord("C", "IV"))  # --> "F"
print(ermittel_akkord("d", "VI"))  # --> "Bb"

"""

# Mapping der Dur- und Moll-Akkorde für die Stufen I bis VII
dur_romannumerale = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
moll_romannumerale = ["i", "ii°", "III", "iv", "v", "VI", "VII"]

# Tonarten und deren zugehörige Akkorde
tonarten_akkorde = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "f": ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb", "Fdim"],
    "d": ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C", "Ddim"],
    "g": ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F", "Gdim"],
    "c": ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb", "Cdim"],
    "a": ["Am", "Bdim", "C", "Dm", "Em", "F", "G", "Adim"],
    "e": ["Em", "F#dim", "G", "Am", "Bm", "C", "D", "Edim"],
    "b": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A", "Bdim"],
    "f#": ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E", "Fdim"],
    "c#": ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B", "Cdim"],
}

def ermittel_akkord(tonart, romannumerale):
    # Überprüfe, ob es sich um Dur oder Moll handelt
    if tonart.islower():
        romannumerale_list = moll_romannumerale
    else:
        romannumerale_list = dur_romannumerale

    # Finde den Index des Romannumerals in der Liste
    index = romannumerale_list.index(romannumerale)

    # Gib den entsprechenden Akkord aus der Tonarten-Akkorde-Liste zurück
    return tonarten_akkorde[tonart][index]

# Beispiele
print(ermittel_akkord("G", "I"))  # --> "G"
print(ermittel_akkord("f", "ii°"))  # --> "Gdim"
print(ermittel_akkord("C", "IV"))  # --> "F"
print(ermittel_akkord("d", "VI"))  # --> "Bb"
