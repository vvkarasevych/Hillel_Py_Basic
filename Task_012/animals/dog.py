from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int):
        #  Initialization of superClass Animal
        super().__init__(f"Dog {name}", {"рыба", "мясо"}, age)
        self.say_word = "Аф"

    def treat(self) -> str:
        """
        Function that describe the process of petting of the dog
        :return: "meat?"
        """
        print(f"Вы ухаживаете за {self.name} и Dog даёт дичь!")
        return "Тушка дичи"
