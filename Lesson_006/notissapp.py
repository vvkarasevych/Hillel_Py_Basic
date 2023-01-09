#  function to show amount of notes which will choose the user
def amount_of_notes(list_to_function: list):
    #  The loop to find the right variable from the user
    while True:
        #  We should use "Try" because we are trying to convert user's input to int.
        try:
            #  asking user to enter data and converting it immediately
            amount_notes_var = int(input("How many notes would you like to see? "))
            #  if user entered less than 1 - we should say about that.
            if amount_notes_var < 1:
                print("Enter, please, the right number! For Example: Integer")
            #  if user entered more than 1 - we need to compare it with the number of elements in a list.
            else:
                #  comparing or we will have an error trying to show more elements than list has.
                if checking_list_and_notes(list_to_function) >= amount_notes_var:
                    return amount_notes_var
#  if something goes wrong - we write about it and...repeat because we have a loop
                else:
                    print("It seems you want to see more, than you have!")
        except (Exception,):
            print("Enter, please, the right number! For Example: Integer")


#  function to compare length of the list and amount of notes what user wants to see.
def checking_list_and_notes(list_to_function: list):
    #  we receive a list and returning the numbers of its elements.
    checking_list_len_var = len(list_to_function)
    return checking_list_len_var


#  function of adding note to the list.
def add_note(list_to_function: list):
    new_note_var = input("Please enter the note: ")
    list_to_function.append(new_note_var)


#  function of sorting "the earliest"
def sorting_earliest(list_to_function: list):
    answer = amount_of_notes(list_to_function)
    for elements in list_to_function[:answer]:
        print(elements)


#  function of sorting "the latest"
def sorting_latest(list_to_function: list):
    #  reversing with slice-method
    temporary_list = list_to_function[::-1]
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


#  function of sorting "the longest"
def sorting_longest(list_to_function: list):
    #  sorting by key and reverse.
    temporary_list = sorted(list_to_function, key=len, reverse=True)
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


#  function of sorting "the shortest"
def sorting_shortest(list_to_function: list):
    temporary_list = sorted(list_to_function, key=len)
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


#  The main part of the Note-Application
if __name__ == '__main__':
    #  we make a list which will have all our notes.
    many_many_notes_list = []
    #  Let's make a loop
    while True:
        print("Choose something:| add | earliest | latest | longest | shortest | exit |")
        #  The user can choose what action application should do.
        decision = input("What would you like to do? ")
        #  The long decision-list
        if decision == "exit":
            exit(0)
        elif decision == "add":
            add_note(many_many_notes_list)
        elif decision == "earliest":
            sorting_earliest(many_many_notes_list)
        elif decision == "latest":
            sorting_latest(many_many_notes_list)
        elif decision == "longest":
            sorting_longest(many_many_notes_list)
        elif decision == "shortest":
            sorting_shortest(many_many_notes_list)
        else:
            #  if the user write the word which is not in an action-list, we will say to the user about that.
            print("I do not understand you! Write exactly what you see.")
