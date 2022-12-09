# Home-task 4

# We need to receive data from the user:

# What needs to know how many liters the car eats.
fuel_per_hundred = input("How many liters fuel is consumption of your car per 100 km? ")
# check if user enters the numbers
try:
    fuel_per_hundred = float(fuel_per_hundred)
    # I do know how to check a number if it is adequate.
    # let it be less than 100 liter per 100 km.
    if 100 < fuel_per_hundred:
        print("It seems you made a mistake - try one more time!")
        exit()
    else:
        pass
except (Exception,):
    print("It seems you made a mistake - try one more time!")
    exit()

# input the price for 1 Liter
fuel_price = input("Please, enter, the price of the current fuel for ONE Liter: ")
# check if user enters the numbers
try:
    fuel_price = float(fuel_price)
    # I do know how to check a price if it is adequate.
except (Exception,):
    print("It seems you made a mistake - try one more time!")
    exit()

# input the distance
distance = input("Please, enter, the distance in km: ")
# check if user enters the numbers
try:
    distance = float(distance)
except (Exception,):
    print("It seems you made a mistake - try one more time!")
    exit()

# formula how many fuel do you need.
how_many_fuel = (distance / 100) * fuel_per_hundred

# formula - how much money you will pay
money = how_many_fuel * fuel_price
money = round(money, 2)
how_many_fuel = round(how_many_fuel, 0)


# Summary
print(f"You need pay {money} UAH to pass {distance} with current consumption of your car...")
