numbers = range(1, 20)

for number in numbers:
    resultby3 = number % 3
    resultby5 = number % 5
    if resultby3 == 0 and resultby5 == 0:
        print("FizzBuzz")
    elif resultby3 == 0 and resultby5 != 0:
        print("Fizz")
    elif resultby5 == 0 and resultby3 != 0:
        print("Buzz")
    else:
        print(number)
