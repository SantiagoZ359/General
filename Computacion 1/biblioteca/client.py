class Client:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Country: {self.country}"
