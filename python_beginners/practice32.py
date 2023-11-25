celebrities = {"Leonardo DiCaprio": "Titanic", "Russel Crow": "Gladiator", "Keanu Reaves": "Matrix"}
another_one = {"Pedro Pascal": "The last of us"}

celebrities.update(another_one)
var_celeb = celebrities.copy()
celebrities.clear()
print(celebrities)
print(var_celeb)
