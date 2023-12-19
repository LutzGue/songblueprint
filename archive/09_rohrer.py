"""
schreibe code in python. benutze klassen.
- es gibt regeln. die wahrscheinlichkeiten werden mit komma separiert und als zahl vorgegeben.
Beispiel:
"key": ("key_C[I{I}][I{I}]",10),("key_G[I{I}][I{I}]",5),("key_D[I{I}][I{I}]",5)
"I": ("[V{V}][I]",10),("",8)
"V": ("[ii{ii}][V]",10),("",8)
... weitere regeln.
- ersetze text innerhalb geschweifter klammern mit den regeln. der text in den geschweiften klammern ist dabei der suchbegriff für die regel. die vorgegebene wahrscheinlichkeit wird bei der zufälligen auswahl berücksichtigt.
Beispiel:
[{key}]
wird umgewandelt in:
[key_C[I{I}][I{I}]]
oder
[key_G[I{I}][I{I}]]
oder
[key_D[I{I}][I{I}]]
- anschließend wird der ersetzungs-mechanismus wiederholt.
Beispiel:
[key_D[I{I}][I{I}]]
wird umgewandelt in:
[key_D[I][I[V{V}][I]]]
oder
[key_D[I[V{V}][I]][I]]
oder
[key_D[I[V{V}][I]][I[V{V}][I]]]
oder
[key_D[I][I]]
- dieser vorgang wieder solange wiederholt, bis keine geschweiften klammern mehr für den ersetzungsprozess vorliegen. zusätzlich werden die anzahl der iterationen gezählt und dürfen den vorgegebenen wert nicht überschreiten (z.B. 1000).

Parsetree viewer:
http://www.ironcreek.net/syntaxtree/

Resuls:
1)
[key_D[I][I[V][I]]]
[key_D[I D][I[V A][I D]]]

2)
[key_D[I[V[ii][V[ii][V]]][I]][I[V][I]]]
[key_D[I[V[ii Em][V[ii (Em)][V A]]][I D]][I[V A][I D]]]

3)
[key_G[I][I[V][I]]]
[key_G[I G][I[V D][I G]]]

4)
[key_C[I[V[ii[vi][ii]][V[ii][V[ii[vi][ii]][V[ii[vi[V/vi][vi]][ii]][V]]]]][I]][I]]
[key_C[I[V[ii[vi Am][ii Dm]][V[ii (Dm)][V[ii[vi Am][ii Dm]][V[ii[vi[V/vi E][vi Am]][ii Dm]][V G]]]]][I C]][I (C)]]

5)
[key_G[I[V][I]][I[V[ii[vi[V/vi][vi]][ii]][V[ii[vi][ii]][V[ii[vi[V/vi][vi]][ii]][V]]]][I]]]
[key_G[I[V D][I G]][I[V[ii[vi[V/vi B][vi Em]][ii Am]][V[ii[vi Em][ii Am]][V[ii[vi[V/vi B][vi Em]][ii Am]][V D]]]][I G]]]

6)
[key_G[I[V[ii[vi][ii]][V[ii][V]]][I]][I[V[ii][V]][I]]]
[key_G[I[V[ii[vi Em][ii Am]][V[ii (Am)][V D]]][I G]][I[V[ii Am][V D]][I G]]]

7)
[key_G[I[V[V/V][V[ii[vi[V/vi][vi]][ii]][V[ii][V]]]][I]][I]]
[key_G[I[V[V/V A^bor][V[ii[vi[V/vi B^bor][vi Em]][ii Am]][V[ii (Am)][V D]]]][I G]][I (G)]]

8)
[key_G[I][I[V[V/V[V/V/V][V/V]][V]][I]]]
[key_G[I G][I[V[V/V[V/V/V E][V/V A]][V D]][I G]]]

9)
[key_C[I[V[V/V][V[V/V][V[ii[vi[V/vi][vi]][ii]][V]]]][I]][I]]
[key_C[I[V[V/V D][V[V/V (D)][V[ii[vi[V/vi E][vi Am]][ii Dm]][V G]]]][I C]][I (C)]]

10)
[key_D[I[V[ii][V[V/V][V]]][I]][I[V[V/V[V/V/V][V/V[V/V/V][V/V[V/V/V][V/V[V/V/V][V/V[V/V/V][V/V]]]]]][V[ii[vi[V/vi][vi]][ii]][V]]][I]]]
[key_D[I[V[ii Em][V[V/V E][V A]]][I D]][I[V[V/V[V/V/V B][V/V[V/V/V (B)][V/V[V/V/V (B)][V/V[V/V/V (B)][V/V[V/V/V (B)][V/V E]]]]]][V[ii[vi[V/vi F][vi Bm]][ii Em]][V A]]][I D]]]

11)
[key_G[I][I[V[V/V[V/V/V][V/V]][V[ii[vi][ii]][V]]][I]]]
[key_G[I G][I[V[V/V[V/V/V E][V/V A]][V[ii[vi Em][ii Am]][V D]]][I G]]]

----------

Ersetze "x" (Akkord-Namen) mit dem kompletten Pfad des jwlg. Elements inenerhalb der Parse-Tree-Syntax:

Beispiel:

 [key_C[I[V[ii key_C,I,V,ii][V[ii[vi key_C,I,V,V,ii,vi][ii key_C,I,V,V,ii,ii]][V key_C,I,V,V,V]]][I key_C,I,I]][I (key_C,I)]]

"""
import random
import re

class MelodyGenerator:
    def __init__(self, rules):
        self.rules = rules
        self.max_iterations = 1000

    def apply_rules(self, text):
        iterations = 0
        while "{" in text and iterations < self.max_iterations:
            start = text.find("{")
            end = text.find("}", start)
            if start != -1 and end != -1:
                search_term = text[start + 1:end]
                if search_term in self.rules:
                    replacement, probability = random.choice(self.rules[search_term])
                    text = text[:start] + replacement + text[end + 1:]
            iterations += 1
        return text
    
    def apply_rules(self, text):
        iterations = 0
        while "{" in text and iterations < self.max_iterations:
            start = text.find("{")
            end = text.find("}", start)
            if start != -1 and end != -1:
                search_term = text[start + 1:end]
                if search_term in self.rules:

                    # Extrahiere den Text vor dem Komma in rules_description
                    rules_description = [item[0] for item in self.rules[search_term]]

                    # Extrahiere den Wert nach dem Komma in rules_value
                    rules_value = [item[1] for item in self.rules[search_term]]

                    replacement = random.choices(rules_description,weights=rules_value,k=1)

                    # konvertierung von list-item zu string mit .join()
                    text = text[:start] + ''.join(replacement) + text[end + 1:]
            iterations += 1
        return text
    
    def clean_repeated_sequences(self, text):
        cleaned_text = text

        # Suche nach aufeinanderfolgenden sich wiederholenden Sequenzen
        for key in self.rules:
            for replacement, _ in self.rules[key]:
                sequence = re.escape(replacement)
                pattern = rf"({sequence})\1+"
                matches = re.finditer(pattern, cleaned_text)

                # Entferne aufeinanderfolgende sich wiederholende Sequenzen
                for match in matches:
                    cleaned_text = cleaned_text.replace(match.group(), match.group(1))

        return cleaned_text
    
    def generate_melodies(self, initial_text, num_melodies):
        melodies = []
        for _ in range(num_melodies):
            melody = initial_text
            melody = self.apply_rules(melody)
            #melody = self.clean_repeated_sequences(melody)
            melodies.append(melody)
        return melodies
    
# Präferenzen in den Regeln
preferences = {
    "use_tonic_overal": 10,
    "use_dominant_overal": 1,
    "use_major_keys": 10,
    "use_minor_keys": 1,
    "use_modal_keys": 1,
    "use_rel_keys": 10,
    "use_inbetween_sections": 0,
    "use_substitutions": 0,
    "use_borrowed_chords": 0
}
"""
# Syntax / Regeln
rules = {
    "key": [
        ("{key_maj}",       preferences["use_major_keys"]), 
        ("{key_min}",       preferences["use_minor_keys"]), 
        ("key_dorian",      preferences["use_modal_keys"]),
        ("key_phrygian",    preferences["use_modal_keys"]),
        ("key_lydian",      preferences["use_modal_keys"]),
        ("key_mixolydian",  preferences["use_modal_keys"]),
        ("key_locrian",     preferences["use_modal_keys"])
        ],
    "key_maj": [
        ("key_Bb{start_maj}", 5), 
        ("key_F{start_maj}", 5),
        ("key_C{start_maj}", 5), 
        ("key_G{start_maj}", 5), 
        ("key_D{start_maj}", 5)
        ],
    "key_min": [
        ("key_g{start_min}", 5), 
        ("key_d{start_min}", 5),
        ("key_a{start_min}", 5), 
        ("key_e{start_min}", 5), 
        ("key_b{start_min}", 5)
        ],
    "rel_key_maj": [
        ("key_I", 5), 
        ("key_ii",5), 
        ("key_iii",5), 
        ("key_IV",5), 
        ("key_V",5), 
        ("key_vi",5), 
        ("key_vii",5), 
        ("key_bVII",5)
        ],
    "rel_key_min": [
        ("key_i",5), 
        ("key_II",5), 
        ("key_bIII", 5), 
        ("key_iv", 5), 
        ("key_V",  5), 
        ("key_v", 5), 
        ("key_VI", 5), 
        ("key_vii",5)
        ],
    "start_maj": [
        ("[I{I}][I{I}]", preferences["use_tonic_overal"]),
        ("[V{V}][V{V}]", preferences["use_dominant_overal"])
        ],
    "start_min": [
        ("[i{i}][i{i}]", preferences["use_tonic_overal"])
        ],
    "I": [
        ("[V{V}][I x]", 10),
        ("[V{V}][I{I}]", 5),
        ("[I{I}][I{I}]", 3), 
        ("[{rel_key_maj}{I}]", 5),
        (" x", 5)
        ],
    "i": [
        ("[V{V}][i x]", 10),
        ("[V{V}][i{I}]", 5),
        ("[i{I}][i{I}]", 3), 
        ("[{rel_key_min}{i}]", preferences["use_rel_keys"]),
        (" x", 5)
        ],
    "V": [
        ("[ii{ii}][V x]", 10), 
        ("[ii{ii}][V{V}]", 5), 
        ("[V/V{V/V}][V x]", 10),
        ("[V/V{V/V}][V{V}]", 5), 
        ("[V{V}][V x]", 10),
        ("[V{V}][V{V}]", 5), 
        ("[{rel_key_maj}{V}]", preferences["use_rel_keys"]),
        (" x", 5)
        ],
    "ii": [
        ("[vi{vi}][ii{ii}]", 10), 
        (" x", 8)
        ],
    "vi": [
        ("[V/vi][vi{vi}]", 10),
        (" x", 8)
        ],
    "V/V": [
        ("[V/V/V x][V/V x]", 10), 
        ("[V/V/V x][V/V{V/V}]", 5), 
        (" x", 8)
        ]
    # Weitere Regeln hier hinzufügen
}
"""
rules={'REL_KEY': [('I', 10), ('IV', 10), ('V', 10), ('vi', 10), ('ii', 10), ('iii', 10)], 'SONG': [('S{PHRASE}', 10)], 'PHRASE': [('{PHRASE}{PHRASE}', 3), ('[P{START}]', 10)], 'START': [('{PRE}{STAT}{DYN1}{CON1}{CAD1}', 10)], 'PRE': [('[PRE{DPR1}]', 10), ('', 10)], 'STAT': [('[STAT{TPR1}]', 10), ('', 10)], 'DYN1': [('[DYN{DYN2}]', 10), ('', 10)], 'CON1': [('[CON{CON2}]', 10), ('', 10)], 'CAD1': [('[CAD{CAD2}]', 10), ('', 5)], 'TPR1': [('{TPR1}{TPR1}', 10), ('[TPR{TPR2}]', 10), ('[SOP{SOP}]', 4)], 'TPR2': [('[I x]', 10), ('[I x]{TPR3}[I x]', 10)], 'TPR3': [('{TPR3}{TPR3}', 20), ('[I6 x]', 10), ('[I46 x]', 10), ('[iii x]', 10), ('[vi x]', 10), ('[V x]', 10), ('[IV x]', 10), ('[vii x]', 10)], 'SOP': [('[I][IV][V][I]', 10), ('[I][ii][V][I]', 10)], 'DPR1': [('{DPR1}{DPR1}', 10), ('[DPR{DPR2}]', 10)], 'DPR2': [('[V x]', 10), ('[V x]{DPR3}[V x]', 10)], 'DPR3': [('{DPR3}{DPR3}', 10), ('[ii x]', 10)], 'I': [('[I x]', 10)], 'V': [('{V}{V}', 5), ('[V x]', 10)], 'DYN2': [('{DYN2}{DYN2}', 30), ('{DYN3}', 20)], 'DYN3': [('{DYN4}', 10), ('[RKEY{REL_KEY}{DYN4}]', 5)], 'DYN4': [('[I x]', 10), ('[ii x]', 10), ('[iii x]', 10), ('[IV x]', 10), ('[V x]', 10), ('[vi x]', 10), ('[vii x]', 10)], 'CON2': [('[ii x]', 10), ('[IV x]', 10)], 'CAD2': [('[PAC{PAC}]', 10), ('[HC{HC}]', 10), ('[DEC{DEC}]', 10), ('[IC]', 10)], 'PAC': [('[V x][I x]', 10)], 'HC': [('[V x]', 10)], 'DEC': [('[V x][vi x]', 10)]}

# Keysord für Start in der Regel-Liste (z.B. SONG)
#initial_text = "[{key}]"
initial_text = "[{SONG}]"

# Anzahl der zu generierenden Melodien
num_melodies = 5

# MelodyGenerator erstellen und Melodien generieren
melody_generator = MelodyGenerator(rules)
generated_melodies = melody_generator.generate_melodies(initial_text, num_melodies)

# Ausgabe der generierten Melodien
for i, melody in enumerate(generated_melodies):
    print(f"Generated Melody {i + 1}:", melody)
