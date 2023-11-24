# index in lists
# It even works to get the index of a string within a list
indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[0])
print(indexes_example[0][0])

# Access an item of a list of lists
list_of_lists = [["one", "two", "three"], [1, 2, 3]]
print(list_of_lists[0][0])

# negative indexes
negative = [1, 2, 3, 4]
print(negative[-1])
print(negative[-4])

# access items and use them in expressions
mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")

# list slicing
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

# reassign items of a list
example = [1, 2, 3, 4]
print(example)
example[3] = 10
example[1:4] = [20, 30, 30]
print(example)
example[4:7] = [100, 200, 350]
print(example)
