# to justify a string either to the left or right
print("Hello World".rjust(15))
print("Hellow wold".ljust(15) + "four spaces.")

print("Hello World".rjust(15, "-"))
print("Hellow wold".ljust(15, "*") + "four spaces.")

print("Hellow World".center(16, "*"))

# remove characters from a string
print("I had an exciting trip!!!!1111")
print("I had an exciting trip!!!!1111".strip("1"))
print("I had an exciting trip!!!!1111".rstrip("1"))
print("I had an exciting trip!!!!1111".lstrip("1"))

# remove words
print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef, bread".lstrip("juice ,"))
print("blueblueyellowblue".strip("eulb"))

# the replace method
print("Good morning.".replace("morning", "afternoon"))

# get the lenght of a string
print(len("tree"))
