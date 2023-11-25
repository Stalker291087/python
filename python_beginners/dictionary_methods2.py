# add key/values to an empty dictionary
groups = {}.fromkeys(["address"], "Fraijanes, Alajuela")
# this will assign each letter as key in the dictionary and the same value for all
groups2 = {}.fromkeys("abc", "Alajuela")
print(groups)
print(groups2)

# pop method
cars = {"make": "Mitsubishi", "model": "Montero Sport", "year": 2021}
model = cars.pop("model")
print(cars)
print(model)

# popitem to remove the last item for the dictionary
cars.popitem()
print(cars)
