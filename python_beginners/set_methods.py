# add method
scifi = {"star trek", "star wars", "halo"}
mountains = {"Everest", "Kilimanjaro", "Fuji"}

scifi.add("mass effect")

print(scifi)

# remove method
scifi.remove("star trek")
print(scifi)

# discard method, does the same as remove but if an item is not found in the set, it doesn't error out

scifi.discard("crysis")
print(scifi)

# clear method, clears the set
games = scifi
#games.clear()
print(games)
print(scifi)

# copy method copies a set into another variable with its own reference in memory
mountains_2 = mountains.copy
print(mountains is mountains_2)

# union method allows to combine 2 sets
all_sets = mountains.union(scifi)
print(all_sets)

# this can also be acomplished with pipe
another_set = mountains | scifi
print(another_set)

# intersection method allows to find out what items two sets have in common
numeric_set_1 = {4, 5, 6, 7, 8}
numeric_set_2 = {6, 7, 8, 9, 10}
new_set = numeric_set_1.intersection(numeric_set_2)
print(new_set)
# same can be acomplished with &
new_set_2 = numeric_set_1 & numeric_set_2
print(new_set)

# substration and difference methods
numeric_set_3 = {4, 5, 6, 7, 8}
numeric_set_4 = {6, 7, 8, 9, 10}
numeric_set_5 = numeric_set_3 - numeric_set_4
print(numeric_set_4)
# same can be acomplished with the difference method
numeric_set_6 = numeric_set_3.difference(numeric_set_4)
print(numeric_set_6)
