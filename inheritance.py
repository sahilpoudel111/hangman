class Car:
    def __init__(self, windows, doors, enginetype) -> None:
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def driving(self):
        print("Car is used for drivilng")


class Audi(Car):
    def __init__(self, windows, doors, enginetype,speed) -> None:
        super().__init__(windows, doors, enginetype)
        self.speed=speed
    
    def selfdriving(self):
        print("It is a selfdriving car")
audiq7=Audi(4,5,"petrol",200)

print(audiq7.speed)
print(audiq7.windows)
audiq7.driving()
audiq7.selfdriving()

car1=Car(4,5,"Diesel")
print(car1)
print(audiq7)

print(dir(car1))