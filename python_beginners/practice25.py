stringValue = input("Type your string: ")

def wordCounter(phrase):
    numberWords = len(phrase.split(" "))
    print(str(numberWords))

wordCounter(stringValue)