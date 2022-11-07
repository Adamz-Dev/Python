class Car():
    brand=""
    model=""
    year=""
    speed=0
    mileage=0
    def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year

class ElectricCar(Car):
    battery_capacity = 0

class C_engine(Car):
    engine_capacity = 0

car = Car("Tesla", "Model Y", 2020)
car.year = 2020

electric_car = ElectricCar("Tesla", "Model S", 2021)
electric_car.battery_capacity = 2000

c_engine_car = C_engine("Toyota", "corolla", 2022)
c_engine_car.brand ="Toyota"


print(f"Electric car brand: {electric_car.brand}")


