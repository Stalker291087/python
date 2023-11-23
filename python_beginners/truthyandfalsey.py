string_example = input("Enter any string other than an empty one: ")

if string_example:
    print("Thank you for entering something.")
else:
    print("You did not enter a string.")

# will tell you the truthy or falsey value of any value
print(bool(0))
print(bool(""))