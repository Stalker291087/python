# lower case letters
all_low = "there are no capitals here."
print(all_low.upper())
print(all_low)

# upper case letters
all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())
print(all_up)

# identify if a string is upper or lower
print(all_up.isupper())
print(all_low.islower())

# use multiple methods
print(all_low.upper().isupper())
print(all_low.upper().islower())

# Other methods
print("Batman".isalnum())
print("123".isdecimal())
print(" ".isspace())
print("The Empire Strikes Back".istitle())

# startswith and endswith methods
print("This is a string".startswith("This"))
print("To infinity and beyond!".endswith("!"))

# join method
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("***".join(["one", "two", "three"]))

#split method
print("Eggs, Milk, Waffles, Bacon".split())
print("Eggs, Milk, Waffles, Bacon".split(","))
print("Eggs, Milk, Waffles, Bacon".split(", "))
