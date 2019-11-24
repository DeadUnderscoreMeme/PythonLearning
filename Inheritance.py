
class Dog:

    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def run(self):
        return self.Name + " is Running"


Dog1 = Dog("Henry",5)

print(Dog1.run())

