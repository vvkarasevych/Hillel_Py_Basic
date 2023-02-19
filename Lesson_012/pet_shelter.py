#  Написати клас собака (Dog), схожий до класу кішка (Cat) з запису заняття.
#  Інтегрувати клас собака до приюту домашніх питомців
#  (скористатись файлом https://github.com/kyrrylo/learn-python-hillel-30-11-2022/blob/main/lesson_12/pet_shelter.py
#  та доповнити його).

from dog import Dog
import random
from datetime import datetime, timedelta

if __name__ == '__main__':
    # create Dogs
    dogs = list()
    dogs_food = ["bones", "meat", "table food", "Pedigree", "Club4Paws"]
    dogs_name = ["Ball", "Sharky", "Baron", "Konig", "Merlin", "Pinky", "Sadly", "Bred", "Sisi", "Princess"]
    dogs_breed = ["Poodle", "Spaniel", "French bulldog", "Chow chow", "Shar-pei", "Shiba inu"]
    last_vet_check = datetime.now()
    for name in dogs_name:
        last_vet_check -= timedelta(days=30)
        dogs.append(Dog(
            name=name,
            gender=random.choice(["he", "she"]),
            age=random.randint(1, 15),
            breed=random.choice(dogs_breed),
            preferable_meal=set(random.choices(dogs_food)),
            last_vet_check=last_vet_check
        ))

    # performing pet everyday lifestyle
    for dog in dogs:
        dog.sleep(random.randint(1, 6))
        for food in random.choices(dogs_food, k=3):
            #  If the dog has ate = we receive True and break the loop - We have no need to show other food
            if dog.eat(food):
                break
            #  else - the food is wrong for the dog we receive False -- we continue the loop. We must show other food
            else:
                continue
        dog.walking(random.randint(2, 6))

    # check if all pets are good
    for dog in dogs:
        print(f"let's check the dog! {dog}")
        if not dog.fed_check:
            if dog.gender == "he":
                print(f"Warning! {dog.name}, he is hungry!")
            elif dog.gender == "she":
                print(f"Warning! {dog.name}, she is hungry!")
            else:
                print(f"{dog.name} - unknown gender {dog.gender}!")
        if not dog.vet_check:
            if dog.gender == "she":
                print(f"Warning! {dog.name}, she has not had a medical checkup a long time ago!")
            elif dog.gender == "he":
                print(f"Warning! {dog.name}, he has not had a medical checkup a long time ago!")
            else:
                print(f"{dog.name} - unknown gender {dog.gender}!")
