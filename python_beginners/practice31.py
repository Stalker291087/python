consonats = {}.fromkeys("bcdfghjklmnpqrstvxyz", "consonant")
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chi-fil-A": "Original Chicken Sandwich"}

for key, value in consonats.items():
    print(key, value)

fast_food_items.popitem()
print(fast_food_items)
