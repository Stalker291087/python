birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}

# get the keys with the keys method
print(birth_years.keys())

for key in birth_years.keys():
    print(key)

# get the values with the values method
print(birth_years.values())

for values in birth_years.values():
    print(values)

# get the keys and values
print(birth_years.items())

for key, values in birth_years.items():
    print(key, values)

# convert output of dictorionaries to a list
print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))

# check if a value is contained in a dictionary
print("juan" in birth_years.values())
print("bill" in birth_years.values())

# get method
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("not found")

print(birth_years.get(1975, "value not found"))

# get lenght of a dictionary
print(len(birth_years))