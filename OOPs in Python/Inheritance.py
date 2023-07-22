class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Creating objects of the derived class
dog = Dog("Buddy")

# Accessing methods from the base class (inherited)
dog.eat()        # Output: Buddy is eating.

# Accessing methods from the derived class
dog.bark()       # Output: Buddy is barking.
