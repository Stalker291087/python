stringVariable = "Jean C Espinoza"

print(stringVariable[0])

# string slicing
print(stringVariable[:3])
print(stringVariable[2:5])
print(stringVariable[4:])

# concatenation
concatenated = "R2" + "-" + "D2"
print(concatenated[3])
print(concatenated[1:4])

# slicing doesn't change the variable value
unchanged = "Forrest Gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)