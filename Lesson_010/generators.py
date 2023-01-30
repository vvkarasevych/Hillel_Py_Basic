#  comments

def checking():
    """
    Function to convert user's input into Integer
    :return: Integer
    """
    while True:
        #  We should use "Try" because we are trying to convert user's input to int.
        try:
            #  asking user to enter data and converting it immediately
            user_input = int(input("How many numbers would you like to see? "))
            return user_input
        except (Exception,):
            print("Enter, please, the right number! For Example: Integer")


def fibonacci(number: int):
    """
    Generator (!) to know the Fibonacci number by its index number
    :param number: how many numbers we want to know or show
    :return: we receive one Fibonacci number
    """
    a, b = 1, 1
    for __ in range(number):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    index = checking()
    for elements in fibonacci(index):
        print(elements)
