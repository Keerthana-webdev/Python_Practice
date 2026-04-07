class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Bike(Vehicle):
    def move(self):
        print("Bike is riding 🏍")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

vehicles = [Car(), Bike(), Plane()]

for v in vehicles:
    v.move()