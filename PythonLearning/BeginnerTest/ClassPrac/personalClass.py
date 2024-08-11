class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Introduce Method
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} year old.")

person1 = Person("Amyra", 4.5)

person1.introduce()