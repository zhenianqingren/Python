class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  # First character upper

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    # f""  f reprensents string

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer += miles
        else:
            print("illegal operation")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


class Electrical_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        else:
            range = 315
        print(f"This car can go about {range} miles on a full range")