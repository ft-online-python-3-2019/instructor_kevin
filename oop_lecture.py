# OOP
# Object Oriented Programming
# A design pattern (not a solution to a problem, but a widely used way to approach solving the problem)
# OOP aims to make our code more organized and easier to understand
# OOP organizes code into discrete objects which have attributes and methods to interact with one another
class Car:
    # body type, color, name, mileage, speed are attributes of cars
    def __init__(self, color, body_type, name):
        self.body_type = body_type
        self.color = color
        self.name = name
        self.mileage = 0
        self.speed = "0mph"
        self.damage = 0
    # drive is a method on a car (function that exists on instances of objects)
    def drive(self, miles_driven):
        self.mileage += miles_driven
    def crash(self, other_car):
        self.damage += 100
        other_car.damage += 5

# classes are blueprints, to create instances:
not_my_car = Car("white", "sedan", "Honda Civic")
jerry_jones_chauffeurs_car = Car("black", "sedan", "Rolls Royce Phantom")

print(f"My car is a { not_my_car.name } { not_my_car.body_type }")
print(f"Jerry Jones' chauffeur's car is a { jerry_jones_chauffeurs_car.name } { jerry_jones_chauffeurs_car.body_type }")

tesla = Car("cheetah print", "sedan", "Tesla Model S")
tesla.drive(200)
print(f"Just drove my Tesla, it now has {tesla.mileage} miles on the odometer")
print(not_my_car.mileage)
not_my_car.drive(150)
print(f"Just drove not my {not_my_car.name}, it now has {not_my_car.mileage} miles on the odometer")

not_my_car.crash(tesla)
print(f"After the accident, not my car is {not_my_car.damage}% totalled and the other car is {tesla.damage}% totalled")
