from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Abstract class cannot be instantiated
# animal = Animal()    # This would raise an error

dog = Dog()
dog.sound()     # Output: Bark!

cat = Cat()
cat.sound()     # Output: Meow!
