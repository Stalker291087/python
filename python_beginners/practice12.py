celciusTemp = input("Type the temperature in Celsius: ")


def fahrenheit(celcius):
    fahrenheitTemp = 1.8 * int(celcius) + 32
    return round(fahrenheitTemp, 1)


print("The Fahrenheit equivalent of " + str(celciusTemp) + " degress Celsius is " + str(fahrenheit(celciusTemp)) + ".")