# nested tuples
nested = ((1, 2, 3), (4, 5, 6, ), (7, 8, 9), (10, 11, 12))

print(nested[3]) # access the values of one of the nested tuples
print(nested[0][0])

# count method
repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)

print("The number " + str(repeat[1]) + " repeats " + str(repeat.count(3)) + " times in the tupple")
print("The number " + str(repeat[0]) + " repeats " + str(repeat.count(7)) + " times in the tupple")
print("The number " + str(repeat[-1]) + " repeats " + str(repeat.count(0)) + " times in the tupple")

# index method to retrive the index number
print(repeat.index(0))
