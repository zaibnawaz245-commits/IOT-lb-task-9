class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")

my_car = Car("Toyota", "Black")
print(my_car.brand, my_car.color)
my_car.start()