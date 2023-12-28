# Mapping der Dur- und Moll-Akkorde für die Stufen I bis VII
dur_romannumerale = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
moll_romannumerale = ["i", "ii°", "III+", "iv", "V", "VI", "vii°"]

# Tonarten und deren zugehörige Akkorde
tonarten_akkorde = {
    "Cb": ["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbdim"],
    "Gb": ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"],
    "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "Cb": ["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbdim"],
    "d#": ["D#m", "E#dim", "F#+", "G#m", "A#", "B", "C#dim"],
    "g#": ["G#m", "A#dim", "B+", "C#m", "D#", "E", "F#dim"],
    "c#": ["C#m", "D#dim", "E+", "F#m", "G#", "A", "Bdim"],
    "f#": ["F#m", "G#dim", "A+", "Bm", "C#", "D", "Edim"],
    "b": ["Bm", "C#dim", "D+", "Em", "F#", "G", "Adim"],
    "e": ["Em", "F#dim", "G+", "Am", "B", "C", "Ddim"],
    "a": ["Am", "Bdim", "C+", "Dm", "E", "F", "Gdim"],
    "d": ["Dm", "Edim", "F+", "Gm", "A", "Bb", "Cdim"],
    "g": ["Gm", "Adim", "Bb+", "Cm", "D", "Eb", "Fdim"],
    "c": ["Cm", "Ddim", "Eb+", "Fm", "G", "Ab", "Bbdim"],
    "f": ["Fm", "Gdim", "Ab+", "Bbm", "C", "Db", "Ebdim"],
    "bb": ["Bbm", "Cdim", "Db+", "Ebm", "F", "Gb", "Abdim"],
    "eb": ["Ebm", "Fdim", "Gb+", "Abm", "Bb", "Cb", "Dbdim"]
}

def ermittle_akkord(tonart, romannumerale):
    # Überprüfe, ob es sich um Dur oder Moll handelt
    if tonart.islower():
        romannumerale_list = moll_romannumerale
    else:
        romannumerale_list = dur_romannumerale

    # Finde den Index des Romannumerals in der Liste
    index = romannumerale_list.index(romannumerale)

    # Gib den entsprechenden Akkord aus der Tonarten-Akkorde-Liste zurück
    return tonarten_akkorde[tonart][index]

def ermittle_mögliche_tonarten(akkord):
    mögliche_tonarten = []

    # debug:
    mögliche_tonarten.append('chord: '+akkord)
    
    for tonart, akkorde in tonarten_akkorde.items():
        if akkord in akkorde:
            # Überprüfe, ob es sich um Dur oder Moll handelt
            if tonart.islower():
                romannumerale_list = moll_romannumerale
            else:
                romannumerale_list = dur_romannumerale
            
            # Überprüfe, ob der Akkord in der Liste vorhanden ist
            if akkord in akkorde:
                # Finde den Index des Akkords in der Tonarten-Akkorde-Liste
                index = akkorde.index(akkord)
                
                # Überprüfe, ob der Index innerhalb der gültigen Bereich liegt
                if index < len(romannumerale_list):
                    # Füge die Tonart und das entsprechende Roman Numeral zur Liste hinzu
                    mögliche_tonarten.append(f"{tonart}-{romannumerale_list[index]}")
    
    return mögliche_tonarten

# Beispiel
# (tonart:"f#", roman:"V") --> ['chord: C#', 'F#-V', 'f#-V']
# (tonart:"f#", roman:"VI") --> ['chord: D', 'G-V', 'D-I', 'A-IV', 'g-V', 'f#-VI']
print(ermittle_mögliche_tonarten(ermittle_akkord("f#", "VI"))) 
