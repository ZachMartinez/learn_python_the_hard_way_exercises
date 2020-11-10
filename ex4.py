# Total number of cars.
cars = 100
# Number of people that can fit inside a car.
space_in_a_car = 4.0
# Total number of drivers.
drivers = 30
# Total number of passengers who don't drive.
passengers = 90
# Number of cars not being driven.
cars_not_driven = cars - drivers
# Number of cars being driven.
cars_driven = drivers
# Number of passengers that can carpool.
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers that need to be in one car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
