import csv

from uuid import uuid4

tech_inventory_dict = dict()

# рписвоить каждому товару уникальный ИД
with open('tech_inventory.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product_id = uuid4()
        tech_inventory_dict[product_id] = {
            'model': row['model'],
            'category': row['category'],
            'brand': row['brand'],
            'price': row['price'],
        }

# создали перечни товаров по категории и бренду (создали индексы на бренд и категорию)
categories_dict = dict()
brands_dict = dict()

for key, value in tech_inventory_dict.items():
    category = value['category']
    brand = value['brand']

    if category not in categories_dict:
        categories_dict[category] = [key]
    else:
        list_of_products = categories_dict.get(category)
        list_of_products.append(key)
        categories_dict[category] = list_of_products

    if brand not in brands_dict:
        brands_dict[brand] = [key]
    else:
        list_of_products = brands_dict.get(brand)
        list_of_products.append(key)
        brands_dict[brand] = list_of_products

# Вывели кол-во товаров по категориям
for k, v in categories_dict.items():
    print(f'{k}: {len(v)} шт')

# Вывели кол-во товаров по брендам
for k, v in brands_dict.items():
    print(f'{k}: {len(v)} товаров')

# Выводим всю информацию о товаре по заданному бренду и категории
brand = input('Enter brand: ')  # Samsung
category = input('Enter product category: ')  # Smartphones

for k, v in tech_inventory_dict.items():
    if v['brand'] == brand and v['category'] == category:
        print(f"id = {k}, brand = {v['brand']}, model = {v['model']}, category = {v['category']}, price = {v['price']}")

# Выводим распределение товаров по категории и бренду
category_brand_inventory_dict = dict()

for key, value in tech_inventory_dict.items():
    category = value['category']
    brand = value['brand']

    if category not in category_brand_inventory_dict:
        category_brand_inventory_dict[category] = {brand: 1}
    else:
        brands_inventory_dict = category_brand_inventory_dict[category]
        if brand not in brands_inventory_dict:
            brands_inventory_dict[brand] = 1
            category_brand_inventory_dict[category] = brands_inventory_dict
        else:
            brands_inventory_dict[brand] += 1
            category_brand_inventory_dict[category] = brands_inventory_dict

for k, v in category_brand_inventory_dict.items():
    print('*' * 50)
    print(f'Категория: {k}')
    for k1, v1 in v.items():
        print(f'{k1}: {v1} шт')