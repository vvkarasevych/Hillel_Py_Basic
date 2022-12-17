#  communication simulation
print("This is the first Chat Bot!")
print("Example of inputting datas: ")

# My PEP8 thinks ukrainian words like a light mistakes.
print("Привіт / Як справи? / Що робиш? / Чим займаєшся / Фільм / Серіал / Бувай")

#  I will use loop "While"
while True:
    #  ask user to enter question or just a sentence
    user_ask = input("You are writing...: ")
    #  a very long list of comparison
    if "бувай" in user_ask.lower() or "надобраніч" in user_ask.lower() or "гудбай" in user_ask.lower():
        print("Побачимось у мережі, I'll be back.")
        break
    elif "привіт" in user_ask.lower() or "хай" in user_ask.lower() or "доброго дня" in user_ask.lower():
        print("Доброго вечора, я бот з України!")
    elif "як справи" in user_ask.lower() or "що робиш" in user_ask.lower() or "чим займаєшся" in user_ask.lower():
        print("Вчусь програмувати на Python!")
    elif "фільм" in user_ask.lower() or "кінотеатр" in user_ask.lower() or "серіал" in user_ask.lower():
        print("Соррі, що втручуюсь, не знаю про що мова, але подивіться серіал \"Wednesday\", він просто бомба!")
    else:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
