class Driver:
    def __init__(self, a_name, drivers_license_category, age):
        self.drivers_license_cat = drivers_license_category
        self.name = a_name
        self.age = age
        self.health = 100
class Car:
    def __init__(self, color, body_type, name, drivers_name, drivers_age):
        self.body_type = body_type
        self.color = color
        self.name = name
        self.mileage = 0
        self.speed = "0mph"
        self.damage = 0
        # driver attribute
        self.motorist = Driver(a_name=drivers_name, drivers_license_category="Class C", age=drivers_age)
    def drive(self, miles_driven):
        if self.motorist.age <16:
            self.crash()
        else:
            self.mileage += miles_driven
    def crash(self):
        self.damage += 100
        self.motorist.health -= 5

car_and_driver = Car("white", "sedan", "Acura TSX", "Kevin", 27)
lil_tays_car = Car("red", "coupe", "Ferrari 458", "Lil Tay", 10)
lil_tays_car.drive(1)
print(lil_tays_car.motorist.health)