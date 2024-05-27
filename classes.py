class Car:
    #constructor
    def __init__(self,windows,tyres, engine) -> None:
        self.windows=windows
        self.tyres=tyres
        self.engine=engine
    def self_driving(self):
        print("The car type is {} engine".format(self.engine))

car1=Car(4,4,"petrol")
print("The number of tyre in car1 is {}".format(car1.tyres))
print("The number of windows in car1 is {}".format(car1.windows))
car1.self_driving()