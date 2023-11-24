console = {"nintendo": "wii", "sony": "playstation"}

print(console["nintendo"])
val = console["sony"]
print(val)

# different type of dictionaries
dictionary_1 = {9: "corundum", 10: "diamond"}
dictionary_2 = {1.23: 1000, 3.14: 1000, 2.178: 100000}
dictionary_3 = {"string": 1, 10210: 2, 4.976: 3, False: 4}

# dictionaries are unordered
# meaning they are equivalent even if they are not ordered the same

# in and not in
print("string" in dictionary_3)
print("jean" not in dictionary_3)
