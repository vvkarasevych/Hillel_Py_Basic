from datetime import datetime


class Dog:
    def __init__(self, name: str, age: int, gender: str, breed: str, preferable_meal: set, last_vet_check):
        """
        Dogs, describe the main facts about life.
        :param name: the name of the dog
        :param age: the age of the dog
        :param gender: he or she?
        :param breed: Breed of dog
        :param preferable_meal: What will the dog eats with pleasure
        :param last_vet_check: When we checked the health
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.fed_check = True
        self.walk_check = True

        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        """
        The common description of the dog.
        :return: The full description.
        """
        return f"{self.name} is the {self.breed}, {self.gender} is {self.age} years old" \
               f' and usually eats {", ".join(self.preferable_meal)}'

    def sleep(self, hours: int):
        """
        Describe the sleeping and depending on the age
        :param hours: how many hours will sleep the dog?
        :return: nothing, print the duration of sleeping
        """
        if self.age > 3:
            hours += 2
        elif self.age > 8:
            hours += 4
        print(f"{self.name} had been sleeping {hours} hours...")

    def eat(self, food):
        """
        Describe the act of eating and the dog will woof, if food does not be liked by dog
        :param food: Food, which will be shown to the dog
        :return: True - if the dog has ate food, False - if the dog does not do that.
        """
        if food in self.preferable_meal:
            print(f"{self.name} eats {food} with pleasure")
            self.fed_check = True
            return True
        else:
            print(f"{self.name} goes though the {food}")
            self.woof(3)
            self.fed_check = False
            return False

    def woof(self, count: int):
        """
        Just woof-woof function
        :param count: How many times will the dog woofing
        :return: nothing
        """
        print(f"{self.name} has woofed {count} times!!")

    def walking(self, hours: int):
        """
        Describe the act of walking
        :param hours: How many hours walks the dog
        :return: nothing
        """
        if self.fed_check:
            print(f"{self.name} goes for a walk with pleasure!")
            self.walk_check = True
        elif not self.fed_check and hours <= 2:
            print(f"{self.name} is hungry, but {self.gender} will go.")
            self.walk_check = True
        else:
            print(f"{self.name} is hungry and {self.gender} will stay at home.")
            self.walk_check = False
        print(f"{self.name} walked {hours} hours.")
