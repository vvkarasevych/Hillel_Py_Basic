#  The main part of the Note-Application
if __name__ == '__main__':
    #  Let's make a loop
    while True:
        print("Choose something:| add | earliest | latest | longest | shortest | exit |")
        #  The user can choose what action application should do.
        decision = input("What would you like to do? ")
        #  The long decision-list
        if decision == "exit":
            exit(0)
        elif decision == "add":
            pass
        elif decision == "earliest":
            pass
        elif decision == "latest":
            pass
        elif decision == "longest":
            pass
        elif decision == "shortest":
            pass
        else:
            #  if the user write the word which is not in an action-list, we will say to the user about that.
            print("I do not understand you! Write exactly what you see.")
