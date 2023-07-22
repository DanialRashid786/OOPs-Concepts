class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()   # Composition - Car has an Engine

    def start_car(self):
        self.engine.start()

car = Car()
car.start_car()   # Output: Engine started.
