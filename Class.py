class Cars ():
    color= ""
    model= ""
    speed= ""
    brand=""
    fuel_tank=""
    number_of_wheel=""
    engine_size=""
    mileage=""

    def current_speed(self):
        print(f"current speed is {self.speed}")
        
    def navigation(self, direction):
        print(f"turn {direction}")
        

car= Cars()
car.brand="Tesla"
car.model="model s"
car.engine_size="4652"
car.fuel_tank="1"
car.number_of_wheel="4"
car.speed="200"

car.current_speed()
car.navigation("left")


    