# global scope variables
example = "Hellow wold"


def loc_ex():
    example = "This is a string"
    return example


print(example)
print(loc_ex())

# global statements
fruit = "apple"


def loc_ex():
    # to use the global variable within the program instead of the local variable fo the function
    global fruit
    fruit = "pear"
    print(fruit)


loc_ex()
print(fruit)
