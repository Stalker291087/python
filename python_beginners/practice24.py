userValue = input("Type your string: ")
emptyString = ""

for i in range(len(userValue) - 1, -1, -1):
    emptyString += userValue[i]

print(emptyString)
