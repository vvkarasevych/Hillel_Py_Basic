# Home-task 3

# We need to receive data from the user:
# What we will have:
brutto_money = input("How much money will you got?: ")
# check if the user entered data we can work.
try:
    brutto_money = float(brutto_money)
except (Exception,):
    print("It seems you made a mistake - try one more time!")
    exit()
# we have to know a percent of taxes.
percent = input("What percent of tax do you have? ")
# check if the user entered data we can work.
try:
    percent = float(percent)
# check! Percents must be less that 100%!
    if percent > 100:
        print("It seems you made a mistake - try one more time!")
        exit()
    else:
        pass
except (Exception,):
    print("It seems you made a mistake - try one more time!")
    exit()

# Formula - how much we will have after taxes.
netto_money = brutto_money - (brutto_money * (percent / 100))
netto_money = round(netto_money, 2)
# Formula - how much we will have to pay.
taxes = brutto_money - netto_money
taxes = round(taxes, 2)

# Summary:
print(f"You will receive: {netto_money} UAH after you pay {taxes} UAH.")
