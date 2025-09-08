# main.py
# Polymorphism: Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

# Superhero inherits from Person
class Superhero(Person):
    def __init__(self, name, age, power, vehicle: Vehicle):
        super().__init__(name, age)
        self.power = power
        self.vehicle = vehicle  # Polymorphism here

    def use_power(self):
        print(f"{self.name} uses {self.power}! 💥")

    def travel(self):
        print(f"{self.name} is on the move:")
        self.vehicle.move()
# Test the classes
if __name__ == "__main__":
    batmobile = Car()
    jet = Plane()

    # Create superheroes
    batman = Superhero("Batman", 35, "Stealth", batmobile)
    superman = Superhero("Superman", 30, "Flight", jet)

    # Introduce and perform actions
    batman.introduce()
    batman.use_power()
    batman.travel()

    print("\n---\n")

    superman.introduce()
    superman.use_power()
    superman.travel()


