#  checking if two indexes exist, we know there must not be the index with minus.
def finder_brackets(line_to_check):
    index_of_left_bracket = line_to_check.find('(')
    index_of_right_bracket = line_to_check.find(')')
    #  just checking the indexes
    #  print(index_of_left_bracket, index_of_right_bracket)
    answer = checking_n_remove(line_to_check, index_of_left_bracket, index_of_right_bracket)
    return answer


def checking_n_remove(text_to_check, index_left, index_right):
    if index_right > index_left > -1 and index_right > -1:
        #  according to the home-task what we must receive we should also delete one space before the bracket.
        #  And we also should plus one to the right index according the syntax of slice-method.
        #  I decided to use "concatenation"
        # upgraded: brackets must be correct left bracket should be the first
        string_to_output = text_to_check[:(index_left - 1)] + text_to_check[(index_right + 1):]
    else:
        print("There are no two brackets which can be acceptable!")
        #  if we do not have two brackets we will just output the string according to the home-task
        print(text_to_check)
        exit(0)
    return string_to_output


#  main part of the application
#  ask user to input information
if __name__ == '__main__':
    #  we need to receive a string from the user
    string_to_check = input("Enter, please, information: ")
    print(finder_brackets(string_to_check))
