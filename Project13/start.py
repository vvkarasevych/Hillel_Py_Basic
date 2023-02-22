from classes import FileProcessor


if __name__ == '__main__':
    allfiles = FileProcessor('SKU')

    for key, value in allfiles.items():
        print(f"{key}, {value}")
