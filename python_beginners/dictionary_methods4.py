# setdefault method is used to look for a key in a dictionary, if the key doesn't exist, it will add it. not to be used to overrride key values
computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro",}

#if "Lenovo" not in computers:
#    computers["Lenovo"] = "Thinkpad"

computers.setdefault("Lenovo", "Thinkpad")
print(computers)

# dict method, gives another way to created a dictionary in python
empty = dict()
list = dict(a=1, b=2, c=3)
print(empty)
print(list)
