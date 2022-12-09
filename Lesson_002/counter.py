# Home-task 2

# input datas of meter
print("What numbers on your meter HAD you?")
data_meter_before = input("Input numbers of your Meter without(!) number after comma: ")
# let's check if user entered what we want: integer.
if data_meter_before.isdigit():
    data_meter_before = float(data_meter_before)
else:
    print("We expected number like Integer.\n"
          "Try one more time, please!")
    exit()

# another part of code for gathering data of user's meter.
print("What numbers on your meter HAVE you NOW?")
data_meter_after = input("Input numbers of your Meter without(!) number after comma: ")
# let's check if user entered what we want: integer.
if data_meter_after.isdigit():
    data_meter_after = float(data_meter_after)
else:
    print("We expected number like Integer.\n"
          "Try one more time, please!")
    exit()

# CHECK! Has the user entered correct datas of Meter? Before must be lower than after!
if data_meter_before > data_meter_after:
    print("It seems you get your meter back! :)\n"
          "If you do not do that - try one more time and be careful!")
    exit()
else:
    pass

# we want to know a price for 1 unit (kwh or cub-meter of water or etc.)
print("How much do you pay for 1 consumed unit?")
price_for_unit = input("Please, enter number like: Integer or Float: ")

# Price must be checked. Trying to convert it in Float.
try:
    price_for_unit = float(price_for_unit)
except (Exception,):
    print("We expected number like Integer or Float.\n"
          "Try one more time, please!")
    exit()

# Formula to know how much we own for consumed units.
we_will_pay = price_for_unit * (data_meter_after - data_meter_before)

# round the number to 2 numbers after comma.
we_will_pay = round(we_will_pay, 2)

print(f"You must pay: {we_will_pay} UAH")
