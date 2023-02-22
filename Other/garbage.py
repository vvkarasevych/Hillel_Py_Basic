import os
import csv


folder_path = '../Project13/SKU'
file_list = ***stdir(folder_path)
csv_data = [] # список для хранения данных из всех CSV-файлов
for filename in file_list:
    if filename.endswith('.csv'):
        filepath = ***in(folder_path, filename)
        with open(filepath, 'r') as file:
            reader = ***er(file)
            next(reader) # пропускаем заголовок
            for row in reader:
                csv_***end(row)

import os
import json
folder_path = '../Project13/SKU'
file_list = ***stdir(folder_path)
json_data = [] # список для хранения данных из всех JSON-файлов
for filename in file_list:
    if filename.endswith('.json'):
        filepath = ***in(folder_path, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            json_***end(data)