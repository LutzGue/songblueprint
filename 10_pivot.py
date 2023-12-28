# Mapping der Dur- und Moll-Akkorde für die Stufen I bis VII
dur_romannumerale = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
moll_romannumerale = ["i", "ii°", "III+", "iv", "V", "VI", "vii°"]

# Enharmonische Gleichheitstabelle
enharmonische_gleichheit = {
    "Cbb": "A#",
    "Cb": "B",
    "C": "C",
    "C#": "C#",
    "Cx": "D",
    "Dbb": "C",
    "Db": "C#",
    "D": "D",
    "D#": "D#",
    "Dx": "E",
    "Ebb": "D",
    "Eb": "D#",
    "E": "E",
    "E#": "F",
    "Ex": "F#",
    "Fbb": "D#",
    "Fb": "E",
    "F": "F",
    "F#": "F#",
    "Fx": "G",
    "Gbb": "F",
    "Gb": "F#",
    "G": "G",
    "G#": "G#",
    "Gx": "A",
    "Abb": "G",
    "Ab": "G#",
    "A": "A",
    "A#": "A#",
    "Ax": "B",
    "Bbb": "A",
    "Bb": "A#",
    "B": "B",
    "B#": "C",
    "Bx": "C#"
}

suffixes = ["m", "dim", "+"]
for suffix in suffixes:
    enharmonische_gleichheit.update({k + suffix: v + suffix for k, v in enharmonische_gleichheit.items()})

# Tonarten und deren zugehörige Akkorde enharmonisch korrekt
tonarten_akkorde_enharmonisch_korrekt = {
    "Cb": (["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbdim"], -7),
    "Gb": (["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"], -6),
    "Db": (["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"], -5),
    "Ab": (["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"], -4),
    "Eb": (["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"], -3),
    "Bb": (["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"], -2),
    "F": (["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"], -1),
    "C": (["C", "Dm", "Em", "F", "G", "Am", "Bdim"], 0),
    "G": (["G", "Am", "Bm", "C", "D", "Em", "F#dim"], 1),
    "D": (["D", "Em", "F#m", "G", "A", "Bm", "C#dim"], 2),
    "A": (["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"], 3),
    "E": (["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"], 4),
    "B": (["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"], 5),
    "F#": (["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"], 6),
    "C#": (["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#dim"], 7),
    "d#": (["D#m", "E#dim", "F#+", "G#m", "A#", "B", "C#dim"], -6),
    "g#": (["G#m", "A#dim", "B+", "C#m", "D#", "E", "F#dim"], -5),
    "c#": (["C#m", "D#dim", "E+", "F#m", "G#", "A", "Bdim"], -4),
    "f#": (["F#m", "G#dim", "A+", "Bm", "C#", "D", "Edim"], -3),
    "b": (["Bm", "C#dim", "D+", "Em", "F#", "G", "Adim"], -2),
    "e": (["Em", "F#dim", "G+", "Am", "B", "C", "Ddim"], -1),
    "a": (["Am", "Bdim", "C+", "Dm", "E", "F", "Gdim"], 0),
    "d": (["Dm", "Edim", "F+", "Gm", "A", "Bb", "Cdim"], 1),
    "g": (["Gm", "Adim", "Bb+", "Cm", "D", "Eb", "Fdim"], 2),
    "c": (["Cm", "Ddim", "Eb+", "Fm", "G", "Ab", "Bbdim"], 3),
    "f": (["Fm", "Gdim", "Ab+", "Bbm", "C", "Db", "Ebdim"], 4),
    "bb": (["Bbm", "Cdim", "Db+", "Ebm", "F", "Gb", "Abdim"], 5),
    "eb": (["Ebm", "Fdim", "Gb+", "Abm", "Bb", "Cb", "Dbdim"], 6)
}

# Tonarten und deren zugehörige Akkorde enharmonisch gleich
tonarten_akkorde = {}
for tonart, akkorde in tonarten_akkorde_enharmonisch_korrekt.items():
    tonarten_akkorde[tonart] = ([enharmonische_gleichheit[akkord] for akkord in akkorde[0]], akkorde[1])

def ermittle_akkord(tonart, romannumerale):
    # Überprüfe, ob es sich um Dur oder Moll handelt
    if tonart.islower():
        romannumerale_list = moll_romannumerale
    else:
        romannumerale_list = dur_romannumerale

    # Finde den Index des Romannumerals in der Liste
    index = romannumerale_list.index(romannumerale)

    # Gib den entsprechenden Akkord und die Quintenzirkel-ID aus der Tonarten-Akkorde-Liste zurück
    return tonarten_akkorde[tonart][0][index], tonarten_akkorde[tonart][1]

def ermittle_mögliche_tonarten(akkord,qzid=0):
    mögliche_tonarten = []

    for tonart, (akkorde, quintenzirkel_id) in tonarten_akkorde.items():
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
                    # Füge die Tonart, das entsprechende Roman Numeral und die Quintenzirkel-ID zur Liste hinzu
                    distance = abs(qzid - quintenzirkel_id)
                    #mögliche_tonarten.append(f"#{distance} {tonart}:{romannumerale_list[index]}")
                    mögliche_tonarten.append((distance, tonart, romannumerale_list[index]))
    
    # Sortiere die Liste nach der Distanz (aufsteigend)
    mögliche_tonarten.sort()

    return mögliche_tonarten

# Beispiel
# (tonart:"f#", roman:"V") --> ['chord: C#', 'F#-V-6', 'f#-V-6']
# (tonart:"f#", roman:"VI") --> ['chord: D', 'G-V-1', 'D-I-2', 'A-IV-3', 'g-V-1', 'f#-VI-6']

#print(ermittle_akkord("f#", "VI")[0])
#print(ermittle_akkord("f#", "VI")[1])
# ['(#2.) (QZ:-2) Bb:iii', '(#1.) (QZ:-1) F:vi', '(#0.) (QZ:0) C:ii', '(#0.) (QZ:0) a:iv', '(#1.) (QZ:1) d:i']

actkey = "f#"
actroman = "V"
print(ermittle_akkord(actkey, actroman)[0])
print(ermittle_mögliche_tonarten(ermittle_akkord(actkey, actroman)[0],ermittle_akkord(actkey, actroman)[1]))
