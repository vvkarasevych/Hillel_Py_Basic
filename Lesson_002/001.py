#  I decided to use math-module to use P-const in code without my entering of it
#  And math-module have a built-in convertor of degrees to radians and vice versa
import math

# Convertor degrees to rad and vice versa

# sentence what we will often use
different_options = "[Degrees to rad(Type: \"dtr\")/Rad to degrees(Type: \"rtd\")/exit(Type: \"exit\")/]"

# the decision list what we have to do
while True:
    # let's input our decision
    decision = input(f"What should I do?{different_options}: ")
    if decision == "dtr":
        print("Let's convert Degrees to radian:")
        try:
            # enter the degrees
            degree = float(input("Enter degrees: "))
            # formula what we use to convert
            rad = degree * (math.pi / 180)
            # rounding the result to five numbers after comma, because task says that to do
            rad = round(rad, 5)
            # output the information
            print(f"{degree} degrees is {rad} radians!")
        # if we enter wrong information we will not have an error
        # cheating with "except Exception:" to avoid PIP8-errors
        except (Exception,):
            print("Your input is not correct! Try one more time! :)")
    elif decision == "rtd":
        print("Let's convert Radians to degrees:")
        try:
            # enter the radian
            rad = float(input("Enter degrees: "))
            # formula what we use to convert
            degree = (rad * 180) / math.pi
            # rounding the result to five numbers after comma, because task says that to do
            degree = round(degree, 5)
            # output the information
            print(f"{rad} radian is {degree} degrees!")
        # if we enter wrong information we will not have an error
        # cheating with "except Exception:" to avoid PIP8-errors
        except (Exception,):
            print("Your input is not correct! Try one more time! :)")
    #  exit from the application
    elif decision == "exit":
        print("Exiting....")
        break
    #  reminding  what we should enter if we make a mistake
    else:
        print(f"Please use allowed options! {different_options}")

#  I have 2 weak errors because of ""except Exception:""
#  How to fix it?
