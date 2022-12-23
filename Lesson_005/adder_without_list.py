#  without list

summa = 0
while True:
    element_float = input("Your number: ")
    try:
        element_float = float(element_float)
        summa += element_float
    except (Exception,):
        if element_float == "sum":
            print(f"Summary of all numbers: {summa}")
            break
        else:
            print("Please enter number or \"sum\"")
