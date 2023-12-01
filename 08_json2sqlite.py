"""
Each row in the table corresponds to a final node from the JSON file. 
The order of the rows in the table corresponds to the order of the last nodes 
in the JSON file.

Dieser Code extrahiert nun die letzten Knoten aus der JSON-Datei basierend auf 
der folgenden Definition: Knoten, die keine weiteren verschachtelten Knoten 
enthalten und sich entweder direkt in der obersten Ebene der JSON-Datei oder in 
einer Liste befinden. Die Reihenfolge der Knoten in der Datenbank wird die gleiche 
sein wie in der JSON-Datei.
"""
import json
import sqlite3

# Funktion zum Durchlaufen der JSON-Daten und Extrahieren der letzten Knoten
def get_last_nodes(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                yield from get_last_nodes(v)
            else:
                yield v
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for k, v in item.items():
                    if not isinstance(v, (dict, list)):
                        yield v

# 1.) Importiere eine JSON datei
with open('pfad_zur_datei.json', 'r') as f:
    data = json.load(f)

# Extrahiere die letzten Knoten aus der JSON-Datei
letzte_knoten = list(get_last_nodes(data))

# 2.) Schreibe die letzten Knoten aus der JSON in eine SQLite datei
conn = sqlite3.connect('datenbankname.db')
c = conn.cursor()

# Erstellen Sie eine Tabelle (wenn sie noch nicht existiert)
c.execute('''CREATE TABLE IF NOT EXISTS tabelle
             (json_data text)''')

# Fügen Sie jeden letzten Knoten in die Tabelle ein
for knoten in letzte_knoten:
    c.execute("INSERT INTO tabelle VALUES (?)", (knoten,))

# Commit (speichern) Sie die Änderungen
conn.commit()

# Schließen Sie die Verbindung
conn.close()
