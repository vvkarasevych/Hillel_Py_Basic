# to read lots of files in the directory
import os
# to process the CSV
import csv
# to process the JSON
import json
# to make different all these data.
from uuid import uuid4


def display_dict(external_dict: dict):
    """
    Just a function to show dict enough not to break eyes...
    :param external_dict:
    :return: nothing
    """
    for key, value in external_dict.items():
        print(f"{key}, {value}")


# make a dict to work with
inner_function_dict = dict()
# loop to read all files
for filename in os.listdir("SKU"):
    # open and nake a path with join to the file in iteration of listdir
    with open(os.path.join("SKU", filename), mode="r", encoding="utf8") as justfile:
        # we compare the extension pf the file to choose what we need to use
        # in this case - CSV-module
        if filename.endswith('.csv'):
            file_object = csv.DictReader(justfile)
            for element in file_object:
                item_id = uuid4()
                # make a structure for data
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
            # we compare the extension of the file to choose what we need to use
            # in this case - JSON-module
            file_object = json.load(justfile)
            file_object = list()
            for element in file_object:
                item_id = uuid4()
                # make a structure for data
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

#  output the information
display_dict(inner_function_dict)
