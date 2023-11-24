import copy
# copy and deepcopy modules
list_of_values = [1, 2, 3, 4, 5]
list_of_values_2 = copy.deepcopy(list_of_values)

list_of_values_2[2] = 10
print(list_of_values)
print(list_of_values_2)

# another way to represent lists
another_list = ["bush",
                "fern",
                "tree",
                "moss"]

print(another_list)

# line continuation character
suma = 2 + \
       4 + \
       1
print(suma)
