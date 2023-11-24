# one important difference between strings and lists is that strings are immutable but lists are mutable
ex_1 = [1, 2, 3]
ex_2 = "123"
ex_3 = "No, you can't"
ex_4 = "Yes" + ex_3[3:11] + "!"

ex_1[1] = 5
print(ex_1)
#ex_2[0] = "2"

# create strings from other strings
print(ex_4)

# references
ex_5 = 3.17
ex_6 = "coconut"
ex_6 = ex_5
ex_7 = ex_6
print(ex_6)
print(ex_7)

# references for lists | if you change the items of a list that was reassigned from a variable, the original variable will also get modified as they are referencing the same list
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)
