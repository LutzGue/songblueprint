"""
schreibe code in python.
- lese text aus input.txt ein. ignoriere beim einlesen zeilen die mit $ zeichen beginnen und zeilen die leer sind.
- die leerzeichen bzw. tabs am anfang der zeilen geben die hierarchie an. speichere die Hierarchieebene jeder zeile als hierarchylevel. entferne im text die vorhergehenden leeren zeichen. füge den wert des hierarchylevel im text als prefix zum text der zeile hinzu und separiere es mit einem semikolon.
- identifiziere texte in geschweiften klammern { }. entferne die geschweiften klammern im text. füge am ende der zeile den text ";replacecandidate" hinzu.
- identifiziere text mit komma zeichen gefolgt von einer zahl. füge  den wert der zahl ans ende der zeile und separiere mit einem semikolon. Entferne im text das komma und die zahl.
- speichere den konvertiereten text als output.csv.
- beispiel der input.txt sieht wie folgt aus:
$ replace method 2

I
    type,10
        {I}
        {I}
    type,10
        {V}
        {I}
    final,10
V
    type,10
        {ii}
        {V}
    type,10
        V/V
        {V}
    final,10
ii
    type,10
        {vi}
        {ii}
    final,10
vi
    type,10
        V/vi
        {vi}
    final,10
key
    Ab,10
    Eb,10
    Bb,10
    F,10
    C,10
    G,10
    D,10
    A,10
SONG
    {key}
    type
        {I}
        {I}
"""
class TextProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process_line(self, line, current_indent):
        # Ignoriere Zeilen, die mit $ beginnen oder leer sind
        if line.startswith('$') or not line.strip():
            return None

        # Entferne Leerzeichen und Tabs am Anfang der Zeilen
        line = line.lstrip()

        # Bestimme den Hierarchielevel
        hierarchylevel = current_indent + 1

        # Entferne geschweifte Klammern und füge ";replacecandidate" am Ende hinzu
        has_brackets = "{" in line and "}" in line
        line = line.replace('{', '').replace('}', '').strip()

        # Identifiziere Text mit Komma und Zahl
        if ',' in line:
            parts = line.split(',')
            value = parts[-1].strip()
            line = ';'.join(parts[:-1] + [value])

        # Füge den Hierarchielevel als Prefix hinzu und separiere mit einem Semikolon
        line = str(hierarchylevel) + ';' + line

        # Füge ";replacecandidate" nur hinzu, wenn geschweifte Klammern vorhanden sind
        if has_brackets:
            line += ';replacecandidate'

        return line

    def process_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as infile, open(self.output_file, 'w', encoding='utf-8') as outfile:
            current_indent = 0
            for line in infile:
                processed_line = self.process_line(line, current_indent)
                if processed_line:
                    outfile.write(processed_line + '\n')
                    # Aktualisiere den Hierarchielevel basierend auf der Einrückung der nächsten Zeile
                    current_indent = len(line) - len(line.lstrip())

# Beispielverwendung der Klasse
if __name__ == "__main__":
    processor = TextProcessor(input_file='input.txt', output_file='output.csv')
    processor.process_file()
