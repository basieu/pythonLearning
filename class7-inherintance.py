class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numOfWheels = 4

    def printVehicleInfo(self):
        print("Vehicle info:", self.brand, self.name, self.topSpeed, self.numOfWheels)


vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo()


class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 220
        print("Car info:", self.brand, self.name, self.topSpeed, self.numOfWheels)


car1 = Car("Ford", "Mustang")
# car1.topSpeed = 240

car1.printCarInfo()
car1.printVehicleInfo()