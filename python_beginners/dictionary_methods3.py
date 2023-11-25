# the clear method
dictionary_1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "North Ireland"}
print(dictionary_1)
dictionary_1.clear()
print(dictionary_1)

# create a copy of a dictionary that has its own reference with the copy method
birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}

people = birth_years
people2 = birth_years.copy()
people2[2000] = "Juan"
people[1982] = "madeleine"
print(birth_years)
print(people)
print(people2)

# update method
city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 293000}

city_info.update(population)
print(city_info)
