class Car:
#template used to create a car
    def __init__(self, maker, color, topSpeed): # Constructor 
        self.maker = maker
        self.color = color
        self.topSpeed = topSpeed

    def carSpeedcat(self):
        if self.topSpeed>100:
            print("Car fad hai")
        else:
            print("Kyu li yah bekar car")

car1 = Car("Honda", "Red", 245)
car1.carSpeedcat()
print(car1.color)
