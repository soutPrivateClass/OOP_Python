class Car :
    def __init__(self, input_merk, input_color, input_year, input_model, input_price):
        self.merk = input_merk
        self.color = input_color
        self.year = input_year
        self.model = input_model
        self.price = input_price

    def speed (self,input_speed):
        print(f"This vehicle has {input_speed} km/h")


vehicle1 = Car("Toyota", "Red", 2020, "Manual", 150)

vehicle1.speed(300)