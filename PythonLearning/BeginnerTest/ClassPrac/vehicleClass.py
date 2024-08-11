class Vehical:
    
    def __init__(self, make, model):

        self.make = make
        
        self.model = model

    def get_info(self):
        print(f"Make: [{self.make}], Model: [{self.model}]")

class Truck (Vehical):
    def __init__(self, make, model, payLoadCapacity):

        super().__init__(make, model)

        self.payLoadCapacity = payLoadCapacity
    
    def get_info(self):
        print(f"Make: [{self.make}], Model: [{self.model}], Payload Capacity: [{self.payLoadCapacity}]")
    
truck1 = Truck("Ford",2024, 3)

truck1.get_info()

car1 = Vehical("Hyundai", 2022)

car1.get_info()
