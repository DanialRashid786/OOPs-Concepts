class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f"{self.name} is barking!")

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing object attributes and calling methods
print(dog1.name)    # Output: Buddy
dog2.bark()         # Output: Max is barking!
