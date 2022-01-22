from car import *
# from car import Car,Electrical_Car
# import car
# from car import Electrical_Car as EC

my_new_car=Car("audi","a4",2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Tesla=EC(^)
Tesla=Electrical_Car("tesla","model_s",2019)
print(Tesla.get_descriptive_name())