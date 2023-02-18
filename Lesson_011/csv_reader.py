import csv
from uuid import uuid4


def display_dict(external_dict: dict):
    """
    Just a function to show dict enough not to break eyes...
    :param external_dict:
    :return: nothing
    """
    for key, value in external_dict.items():
        print(f"{key}, {value}")


def open_file_indexing(filename: str):
    """
    The function to open and process the file like csv into dictionary with uniq indexes.
    :param filename: the name of the file
    :return: indexed dictionary with "uuid"
    """
    inner_function_dict = dict()
    with open(filename, mode="r", encoding="utf8") as csvfile:
        file_object = csv.DictReader(csvfile)
        for element in file_object:
            item_id = uuid4()
            inner_function_dict[item_id] = {
                'category': element['category'],
                'brand': element['brand'],
                'model': element['model'],
                'price': element['price'],
            }
        return inner_function_dict


def making_dict(external_dict: dict, new_key: str):
    """
    The function makes dictionaries by current key
    :param external_dict: dictionary to remake
    :param new_key: accept the new key to make more specific dictionary
    :return: remade dictionaries
    """
    inner_dict = dict()
    for key, value in external_dict.items():
        category = value[new_key]
        if category not in inner_dict:
            inner_dict[category] = [key]
        else:
            list_of_products = inner_dict.get(category)
            list_of_products.append(key)
            inner_dict[category] = list_of_products
    return inner_dict


if __name__ == '__main__':
    file = "tech_inventory.csv"
    #  open the file and make the dictionary with indexes.
    indexed_dict = open_file_indexing(file)
    display_dict(indexed_dict)

    #  making dictionary by one category which include all uniq ids.
    category_dict = making_dict(indexed_dict, "category")
    brand_dict = making_dict(indexed_dict, "brand")
    display_dict(category_dict)
    display_dict(brand_dict)

    #  how many units have category and brand.
    for key, value in category_dict.items():
        print(f'In {key} is {len(value)} units.')

    for key, value in brand_dict.items():
        print(f'{key} has {len(value)} units.')

    #  All units in category and brand.
    print("Task to show how many unis is for a brand, for Example \"Logitech\".")
    brand = "Logitech"
    i = 1
    for elements in brand_dict[brand]:
        print(f'{i}. {indexed_dict[elements]}')
        i += 1

    print("Task to show how many unis is for a category, for Example \"Keyboard\".")
    category = "Keyboard"
    i = 1
    for elements in category_dict[category]:
        print(f'{i}. {indexed_dict[elements]}')
        i += 1

    #  How many unit of brand do we have in each category.
    category_brand_inventory_dict = dict()
    for key, value in indexed_dict.items():
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

    for key, value in category_brand_inventory_dict.items():
        print("*" * 40)
        print(f'There are: {key}')
        for key2, value2 in value.items():
            print(f'{key2}: is {value2} units')
