#  we need importing OS to check the file.
import os


def amount_of_notes(list_to_function: list):
    """
    function to show amount of notes which will choose by the user.
    :param list_to_function: the list what we have with notes.
    :return: integer - how many notes will be displayed.
    """
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


def checking_list_and_notes(list_to_function: list):
    """
    function to help comparing the length of the list and amount of notes what user wants to see.
    We will receive a list and returning the numbers of its elements.
    :param list_to_function: the list what we have with notes.
    :return: integer: how many notes we have already in our list.
    """
    checking_list_len_var = len(list_to_function)
    return checking_list_len_var


def add_note(list_to_function: list):
    """
    function of adding note to the list.
    :param list_to_function: the list what we have with notes.
    :return: nothing - we just displayed the the necessary information.
    """
    new_note_var = input("Please enter the note: ")
    list_to_function.append(new_note_var)


def sorting_earliest(list_to_function: list):
    """
    function of sorting "the earliest"
    :param list_to_function: the list what we have with notes.
    :return: nothing - we just displayed the the necessary information.
    """
    answer = amount_of_notes(list_to_function)
    for elements in list_to_function[:answer]:
        print(elements)


def sorting_latest(list_to_function: list):
    """
    function of sorting "the latest"
    :param list_to_function: the list what we have with notes.
    :return: nothing - we just displayed the the necessary information.
    """
    #  reversing with slice-method
    temporary_list = list_to_function[::-1]
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


def sorting_longest(list_to_function: list):
    """
    function of sorting "the longest"
    :param list_to_function: the list what we have with notes.
    :return: nothing - we just displayed the the necessary information.
    """
    #  sorting by key and reverse.
    temporary_list = sorted(list_to_function, key=len, reverse=True)
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


def sorting_shortest(list_to_function: list):
    """
    function of sorting "the shortest"
    :param list_to_function: the list what we have with notes.
    :return: nothing - we just displayed the the necessary information.
    """
    temporary_list = sorted(list_to_function, key=len)
    answer = amount_of_notes(list_to_function)
    for elements in temporary_list[:answer]:
        print(elements)


def open_file_func(name_of_file: str):
    """
    Function to open the file and reading it.
    We will return the LIST with all notes from the current file.
    :param name_of_file: the name of the file we are using.
    :return: list - the list with notes what we have in the file.
    """
    with open(file=name_of_file, mode="r", encoding="utf-8") as file:
        list_to_return = []
        for lines in file:
            list_to_return.append(lines.strip("\n"))
        print(list_to_return)
    return list_to_return


def save_n_exit(name_of_file: str, list_to_function: list):
    """
    Function to save the list with notions in the current file.
    We will receive the name of the file and list with all notes.
    :param name_of_file: the name of the file we are using.
    :param list_to_function: the list with our notes.
    :return: nothing: just save the file.
    """
    with open(file=name_of_file, mode="w", encoding="utf-8") as file:
        for elements in list_to_function:
            file.write(elements + "\n")
    print(f"The file {name_of_file} saved!")
    print("Exiting....")


#  The main part of the Note-Application
if __name__ == '__main__':
    #  declared a list to work
    many_many_notes_list = []
    #  we ask the file name.
    file_name = input("Enter the name of file in the next way - name.extension, for example \"text.txt\": ")

    check_exist = os.access(file_name, os.F_OK)  # check the path to the file
    check_read = os.access(file_name, os.R_OK)  # check if we can read the file

    if check_exist and check_read:
        #  we make a list which will have all our notes.
        many_many_notes_list = open_file_func(file_name)

        #  Let's make a loop
        while True:
            print("Choose something:| add | earliest | latest | longest | shortest | exit |")
            #  The user can choose what action application should do.
            decision = input("What would you like to do? ")
            #  The long decision-list
            if decision == "exit":
                save_n_exit(file_name, many_many_notes_list)
                break
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
    else:
        #  if we do have such file... or we have no permission.
        print("Exists the file:", check_exist)
        print("Access to read the file:", check_read)
        print("Facing some issue!")
