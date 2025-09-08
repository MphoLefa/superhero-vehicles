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

