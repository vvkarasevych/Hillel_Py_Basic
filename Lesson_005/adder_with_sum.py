#  I am using list and sum-function to make a summary

input_list = []

while True:
    element_float = input("Your number: ")
    try:
        element_float = float(element_float)
        input_list.append(element_float)
    except (Exception,):
        if element_float == "sum":
            print(f"Summary of all numbers: {sum(input_list)}")
            break
        else:
            print("Please enter number or \"sum\"")
