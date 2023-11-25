# sets are like lists, but they cannot have duplicate values, it will show only the first item, the values that contains are unordered
set_1 = {9, 8, 7, 6, 6, 6}
set_2 = set({"a", "b", "c", "d", "e"})
set_3 = set(range(1, 12, 2))

print(set_1)
print(set_2)
print(set_3)

# elements of a set, can be accessed with for, but not by index
for num in set_3:
    print(num)

print(0 in set_3)
