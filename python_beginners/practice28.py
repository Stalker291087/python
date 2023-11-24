artic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

del artic_animals[4]
artic_animals.remove("elephant")
artic_animals.append("artic fox")
artic_animals.insert(2 ,"snowy owl")
artic_animals.sort(key=str.lower)

print(artic_animals)
print(artic_animals.index("reindeer"))
last_item = artic_animals.pop()
print(last_item)
