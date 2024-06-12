class Calorie:

    def __init__(self, weight, height, age, temperature) -> None:
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass


class Temperature:

    def __init__(self, country, city) -> None:
        self.country = country
        self.city = city

    def get(self):
        pass
