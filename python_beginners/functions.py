print("this")
print("is")
print("an")
print("example")

# defining a function
def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")


# calling the function
prints_four()


def sumNum(number):
    print(number + 2)


sumNum(4)


# multiple parameters
firstString = "The number "


def printNumber(p1, p2, p3):
    print(p1 + str(p2) + p3)


printNumber(firstString, 5, " is an integer.")


# default parameters and using return
def defaultfunction(num1=7, num2=8):
    return num1 + num2


print(defaultfunction() + 44)
# if you pass parameters, the already defined params are going to be replaced
