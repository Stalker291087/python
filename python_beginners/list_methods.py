planets = ["pluto", "mars", "earth", "venus"]
provincias = ["alajuela", "heredia", "heredia", "heredia", "guanacaste", "limon"]
num_list = [2.718, 4, -19, 10000, 0]
bands = ["passiflora", "magpie jay", "kadeho"]

# remove item in list with del. It uses the index
del planets[0]
print(planets)

# remote method / when trying to remove an item that appears multiple times, it will delete only the first apperance. It uses the value
provincias.remove("heredia")
print(provincias)

# append method to add a value to the end
provincias.append("cartago")
print(provincias)

# insert method, allows you to add an item on the list in any index
provincias.insert(1, "puntarenas")
print(provincias)

# sort is used to sort values that are all strings or numbers
num_list.sort()
print(num_list)
provincias.sort()
print(provincias)
# sort in reverse order
provincias.sort(reverse=True)
print(provincias)

# sort arranges not in alphabetical order but in ASCIIbetical order, meaning that capital letters will go first
# in order to sort in alphabetical order you need to use they key inside the sort method
provincias.sort(key=str.lower)
print(provincias)

# index method helps you to identify the index where a value is stored. if the list has the value more than once, it will show its first appearance
print(provincias.index("heredia"))

# pop method to take one value from the list and assign it to a variable
last_band = bands.pop()
first_band = bands.pop(0)
print(last_band)
print(first_band)
