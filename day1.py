import math
import utils




def calculate_fuel_requirement(mass):
    return math.floor(mass / 3) - 2


def calculate_fuel_requirement_advanced(mass):
    total_fuel = 0
    temp_fuel = calculate_fuel_requirement(mass)
    while temp_fuel > 0:
        total_fuel = total_fuel + temp_fuel
        temp_fuel = calculate_fuel_requirement(temp_fuel)
        print(temp_fuel)
    return total_fuel


# get the input
stringlist = utils.getinput("day1.txt")

# convert to list of ints
masslist = utils.converttofloat(stringlist)

sum_fuel_requirement = 0
for mass in masslist:
    fuel_requirement = calculate_fuel_requirement_advanced(mass)
    sum_fuel_requirement = sum_fuel_requirement + fuel_requirement

print(sum_fuel_requirement)
