# just lots of instruction for the user
print("Just input numbers and decide what you want to do with those numbers:")
print("sum = obtain the summary of all numbers entered by the user.")
print("multi = obtain the multiplication of all number entered by the user.")
print("You can enter any number, for example: 4.5 or 6 or 235.65656")
print("exit = emergency end the application.")

#  I decided to declare the list before using in code
input_user_list = []


#  function to sum all values
def summa(user_list: list):
    #  if user enters only one number we will have the right result if we declare variable as 0.
    summa_float = 0
    #  loop for the list of number, or we can call the sum()-function
    #  summa_float = sum(user_list)
    for elements in user_list:
        summa_float += elements
    #  return the result
    return summa_float


#  function to multiplicative all values
def multiplication(user_list: list):
    #  if the user enter only one number - we will have the right result.
    multiplication_float = 1
    #  loop to multiplication all number of our iteration
    for elements in user_list:
        multiplication_float *= elements
    #  return the result
    return multiplication_float


#  start the loop
while True:
    #  user's input
    element_float = input("Your number: ")
    try:
        #  trying to make float and checking for right input data
        element_float = float(element_float)
        #  add to the list if user's input is correct
        input_user_list.append(element_float)
    except (Exception,):
        #  checking if the user's input was incorrect but simultaneously correct.
        if element_float == "sum":
            #  if user entered word sum - we will call the function "summa" and show to the user result
            print("Summary of all numbers: ", summa(input_user_list))
            #  while-loop - we need to break
            break
        #  checking if the user's input was incorrect but simultaneously correct.
        elif element_float == "multi":
            #  if user entered word multi - we will call the function "multiplication" and show to the user result
            print("Multiplication of all number: ", multiplication(input_user_list))
            #  while-loop - we need to break
            break
        #  check the input for the word "exit"
        elif element_float == "exit":
            exit(0)
        else:
            #  if the user entered the garbage we should say to user about that)))
            #  and do not break the while-loop
            print("Please enter number or action (sum|multi|exit)")
