from jsonpro import JSONFileProcessor
from csvpro import CSVFileProcessor

import os


class FileProcessor:
    def __init__(self, path):
        self.path = path
        self.entries = dict()

    def process(self):
        for filename in os.listdir(self.path):
            if filename.endswith('.csv'):
                csv_file = CSVFileProcessor(os.path.join(self.path, filename))
                self.entries = csv_file
            elif filename.endswith('.json'):
                json_file = JSONFileProcessor(os.path.join(self.path, filename))
                self.entries = json_file
        return self.entries
