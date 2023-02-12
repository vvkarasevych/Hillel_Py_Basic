import csv
from uuid import uuid4

with open('tech_inventory.csv') as f:
    reader = csv.DictReader(f)
    tech_inventory_dict = dict()
    for row in reader:
        product_id = uuid4()
        tech_inventory_dict[product_id] = {
            'model': row['model'],
            'category': row['category'],
            'brand': row['brand'],
            'price': row['price'],
        }

print(tech_inventory_dict)