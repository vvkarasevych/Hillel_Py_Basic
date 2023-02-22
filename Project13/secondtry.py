import os
import csv
import json
from uuid import uuid4


def display_dict(external_dict: dict):
    """
    Just a function to show dict enough not to break eyes...
    :param external_dict:
    :return: nothing
    """
    for key, value in external_dict.items():
        print(f"{key}, {value}")


#
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


class JSONFileProcessor(FileProcessor):
    def __init__(self, path):
        super().__init__(path)
        self.entries = dict()

    def process(self):
        with open(os.path.join(self.path), mode="r", encoding="utf8") as justfile:
            file_object = json.load(justfile)
            file_object = list()
            for element in file_object:
                item_id = uuid4()
                self.entries[item_id] = {
                    "date": element["date"],
                    "time": element["time"],
                    "sku": element["sku"],
                    "warehouse": element["warehouse"],
                    "warehouse_cell_id": element["warehouse_cell_id"],
                    "operation": element["operation"],
                    "invoice": element["invoice"],
                    "expiration_date": element["expiration_date"],
                    "operation_cost": element["operation_cost"],
                    "comment": element["comment"],
                }
        return self.entries


class CSVFileProcessor(FileProcessor):
    def __init__(self, path):
        super().__init__(path)
        self.entries = dict()

    def process(self):
        with open(os.path.join(self.path), mode="r", encoding="utf8") as justfile:
            file_object = csv.DictReader(justfile)
            for element in file_object:
                item_id = uuid4()
                self.entries[item_id] = {
                    "date": element["date"],
                    "time": element["time"],
                    "sku": element["sku"],
                    "warehouse": element["warehouse"],
                    "warehouse_cell_id": element["warehouse_cell_id"],
                    "operation": element["operation"],
                    "invoice": element["invoice"],
                    "expiration_date": element["expiration_date"],
                    "operation_cost": element["operation_cost"],
                    "comment": element["comment"],
                }
        return self.entries


if __name__ == '__main__':
    inner_function_dict = dict()
    inner_function_dict = FileProcessor("SKU")

    display_dict(inner_function_dict)
