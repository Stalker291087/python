import random

gallons_gas = random.randint(10, 25)
miles_travel = random.randint(100, 400)


def miles_per_gallon(gallons, miles):
    milespergallon = miles // gallons
    return str(milespergallon)


print("The car can hold " + str(gallons_gas) + " gallons of gas")
print("The car can travel " + miles_per_gallon(gallons_gas, miles_travel) + " miles with a full tank.")
