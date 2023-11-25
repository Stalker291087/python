# tupples
tupple_1 = ("a", "b", "c", "d", "e")
tupple_2 = (2.718, False, [1, 2, 3])
tupple_3 = (1, 1, 0, 0, 0)
# create tupples by method
tupple_4 = tuple("edcba")
print(tupple_4)

print(tupple_4[0])
# you can also use slicing with tupples
print(tupple_4[0:2])
print(tupple_4[-1])

# tupples are immutable meaning, cannot be changed
tupple_5 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#tupple_5[1] = 24 it doesn't work
# tupples also take less memory
tupple_6 = (1, 2, 3)
list_1 = [1, 2, 3]

print(tupple_6.__sizeof__())
print(list_1.__sizeof__())

# iterating a tuple
major_cities = ("Tokyo", "Londong", "New York", "Shangai", "Sydney")

for cities in major_cities:
    print(cities)

count = 0
while count < len(major_cities):
    print(major_cities[count])
    count += 1

backwards = len(major_cities) - 1
while backwards > -1:
    print(major_cities[backwards])
    backwards -= 1

# slicing a tupples
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(ints[::3])
print(ints[1::2])
print(ints[0:4])
print(ints[5:])
print(ints[7::-1])
