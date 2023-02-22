from fileprocessor import FileProcessor

import os
import json
from uuid import uuid4


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
