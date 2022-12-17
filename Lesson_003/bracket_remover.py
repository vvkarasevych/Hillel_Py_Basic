#  we need to receive a string from the user
string_to_check = input("Enter, please, information: ")

index_of_left_bracket = string_to_check.find('(')
index_of_right_bracket = string_to_check.find(')')

#  just checking the indexes
#  print(index_of_left_bracket, index_of_right_bracket)

#  checking if two indexes exist, we know there must not be the index with minus.
if index_of_left_bracket > -1 and index_of_right_bracket > -1:
    #  according to sentence in the home-task what we must receive we should also delete one space before the bracket.
    #  And we also should plus one to the right index according the syntax of slice-method.
    #  I decided to use "contaminatio"
    string_to_output = string_to_check[:(index_of_left_bracket - 1)] + string_to_check[(index_of_right_bracket + 1):]
    print(string_to_output)
else:
    print("There are no two brackets which can be acceptable!")
    #  if we do not have two brackets we will just output the string according to the home-task
    print(string_to_check)
