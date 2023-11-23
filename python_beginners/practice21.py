number = int(input("Please type an integer value: "))

def factorial(num):
    result = 1
    for numeral in range(num, 1, -1):
        result *= numeral
    return result
        
print(factorial(number))
