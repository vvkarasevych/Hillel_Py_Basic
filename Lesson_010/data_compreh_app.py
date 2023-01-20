#  Task: ['Adxsd', 'Asdjhdx', '']
#  Have: ['gfhdaDSXd\n', 'asdjhdx\n', 'sdjhAxdzx']

if __name__ == '__main__':
    #  Read the file and sign it as "file"
    with open(file="task.txt", mode="r", encoding="utf-8") as file:

        #  For educational purposes only!
        #  I just want to see how exactly look the list after the "read-lines" method
        #  just_to_see = file.readlines()
        #  print(just_to_see)

        #  list comprehension = deleting \n and split the file into lines by "read-lines" method
        new_list = [line.strip("\n") for line in file.readlines()]
        #  Just to see all transformations
        print(new_list)

        #  list comprehension = slicing by "a" and if there is no "a" replace by the empty line.
        new_list_2 = [element[element.find("a"):] if "a" in element else "" for element in new_list]
        #  Just to see all transformations
        print(new_list_2)

        #  list comprehension = to make the first "a" big and others letters make small if its need that.
        new_list_3 = [element.capitalize() for element in new_list_2]
        #  Just to see all transformations
        print(new_list_3)
