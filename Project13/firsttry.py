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
inner_function_dict = dict()
for filename in os.listdir("SKU"):
    with open(os.path.join("SKU", filename), mode="r", encoding="utf8") as justfile:
        if filename.endswith('.csv'):
            file_object = csv.DictReader(justfile)
            for element in file_object:
                item_id = uuid4()
                inner_function_dict[item_id] = {
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
        else:
            file_object = json.load(justfile)
            file_object = list()
            for element in file_object:
                item_id = uuid4()
                inner_function_dict[item_id] = {
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

display_dict(inner_function_dict)
