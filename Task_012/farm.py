#  Додати до ферми
#  https://github.com/kyrrylo/learn-python-hillel-30-11-2022/blob/main/lesson_13/farm.py
#  представника класу собака.

from animals import Cat
from animals import Hen
from animals import Cow
from animals import Dog
import random

if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая'),
        Hen(1),
        Cow('Бурёнка', 4),
        Dog("Шарик", 7)
    ]
    food_variants = [
        'трава',
        'сено',
        'пшено',
        'зерно',
        'рыба',
        'мясо',
        'молоко'
    ]

    what_we_get = list()
    what_they_get = list()
    # Полиморфизм - свойство классов, при котором вызываются одинаково названные методы/атрибуты,
    # но результат вызова отличается
    # например, у классов Cat, Hen, Cow есть одинаково названные атрибуты: name и age
    # так же у этих же классов есть одинаково названные методы eat, treat & say

    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=3):
            a.eat(food)
            what_they_get.append(food)
        what_we_get.append(a.treat())

    #  let's check eat animal or not
    # check if all pets are good
    for a in animals:
        print(f"let's check {a.name}!")
        if not a.fed_check:
            print(f"Warning! {a.name} is hungry!")
        else:
            print(f"{a.name} is ok for today!")

    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')
