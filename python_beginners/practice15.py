import random

num = random.randint(0, 10)

if num == 10:
    print("The roman numeral equivalent of " + str(num) + " is X")
elif num == 9:
    print("The roman numeral equivalent of " + str(num) + " is IX")
elif num == 8:
    print("The roman numeral equivalent of " + str(num) + " is IIX")
elif num == 7:
    print("The roman numeral equivalent of " + str(num) + " is VII")
elif num == 6:
    print("The roman numeral equivalent of " + str(num) + " is VI")
elif num == 5:
    print("The roman numeral equivalent of " + str(num) + " is V")
elif num == 4:
    print("The roman numeral equivalent of " + str(num) + " is IV")
elif num == 3:
    print("The roman numeral equivalent of " + str(num) + " is IIV")
elif num == 2:
    print("The roman numeral equivalent of " + str(num) + " is II")
else:
    print("The roman numeral equivalent of " + str(num) + " is II")
