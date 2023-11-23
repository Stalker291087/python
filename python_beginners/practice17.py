number = int(input("Type an integer: "))

counter = number
summed = 0

while counter > 0:
    summed += counter
    counter -= 1

print("Integer entered by the user is " + str(number))
print("The sum of the while loop is: " + str(summed))
