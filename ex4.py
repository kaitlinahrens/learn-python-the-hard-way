cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex4.py
# There are 100 cars available.
# There are only 30 drivers available.
# There will be 70 empty cars today.
# We can transport 120.0 people today.
# We have 90 to carpool today.
# We need to put about 3 in each car.

# His error was one of lack of attention of detail: he wrote car_pool_capacity instead of carpool_capacity, therefore the variable didn't exist in this script
