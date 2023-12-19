import csv

class CSVConverter:
    def __init__(self, file_path, output_file='output_01.csv', is_mode_debugging=False):
        self.file_path = file_path
        self.output_file = output_file
        self.is_mode_debugging = is_mode_debugging
        self.root = []
        self.levels = {0: self.root}

    def process_line(self, line, levels):
        """
        Process a line from the input file, extracting relevant information and building a hierarchical structure.

        Parameters:
        - line (str): A line from the input file to be processed.
        - levels (dict): A dictionary representing the hierarchical levels of the structure.

        Raises:
        - Exception: If an error occurs during the processing of the line.
        """
        try:
            if len(line.strip()) > 0 and line.strip()[:1] != '$':
                indent = len(line) - len(line.lstrip())
                parts = line.strip().split(',')

                label = parts[0]
                value = int(parts[1]) if len(parts) > 1 and parts[1] else -1
                generatemin = int(parts[2]) if len(parts) > 2 and parts[2] else -1
                generatemax = int(parts[3]) if len(parts) > 3 and parts[3] else -1

                if self.is_mode_debugging:
                    print(indent, label, value, generatemin, generatemax)

                node = {'description': label}

                if '{' in label or '}' in label:
                    node['description'] = label.replace('{', '').replace('}', '')
                    node['isreplacecandidate'] = True
                    node['isreplaced'] = False
                else:
                    node['isreplacecandidate'] = False
                    node['isreplaced'] = False

                node['value'] = value

                if value != -1:
                    node['isprobability'] = True
                else:
                    node['isprobability'] = False

                node['generatemin'] = generatemin
                node['generatemax'] = generatemax

                node['isreplicated'] = False
                node['clonenr'] = 1

                if generatemin != -1 and generatemax != -1:
                    node['isreplicatecandidate'] = True
                    node['isreplicated'] = False
                else:
                    node['isreplicatecandidate'] = False
                    node['isreplicated'] = False

                if indent == 0:
                    node['isoriginal'] = True
                else:
                    node['isoriginal'] = False

                levels[indent].append(node)
                levels[indent + 4] = node.setdefault('children', [])
            else:
                if self.is_mode_debugging:
                    print('skip comment or empty line:', '"' + line + '"')
        except Exception as e:
            print(f"An error occurred while processing line: {line}\nError: {e}")

    def remove_empty_children(self, node):
        if 'children' in node and not node['children']:
            del node['children']
        else:
            for child in node.get('children', []):
                self.remove_empty_children(child)

    def convert_to_csv(self):
        """
        Convert the processed hierarchical structure to a CSV file.

        Parameters:
        - None

        Raises:
        - Exception: If an error occurs during the CSV conversion process.
        """
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    self.process_line(line, self.levels)

            for node in self.root:
                self.remove_empty_children(node)

            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['hierarchieebene', 'description', 'isreplacecandidate', 'isreplaced', 'isprobability', 'probabilityvalue']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()

                def write_csv_row(node, hierarchy_level):
                    writer.writerow({
                        'hierarchieebene': hierarchy_level,
                        'description': f'"{node["description"]}"',
                        'isreplacecandidate': node.get('isreplacecandidate', False),
                        'isreplaced': node.get('isreplaced', False),
                        'isprobability': node.get('isprobability', False),
                        'probabilityvalue': node.get('value', -1)
                    })
                    for child in node.get('children', []):
                        write_csv_row(child, hierarchy_level + 1)

                for node in self.root:
                    write_csv_row(node, 1)
        except Exception as e:
            print(f"An error occurred during CSV conversion. Error: {e}")

# Usage
converter = CSVConverter('input.txt')
converter.convert_to_csv()
