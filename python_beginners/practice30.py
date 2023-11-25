groups = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bod Dylan": "Like a Rolling Stone",}

print("Dictionary lenght is :" + str((len(groups))))

print("\n**Dictionary keys are:** ")
for key in groups.keys():
    print(key)

print("\n**Dictionary values are:** ")
for value in groups.values():
    print(value)

print("\n**All keys and values from the dictionary are:**")
for items in groups.items():
    print(items)

print(groups.get("Promise of the Real", "Value was not found, try again"))
