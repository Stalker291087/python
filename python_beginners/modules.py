# module generic import
import random
# function import
from random import randint
# universal import
from random import *

print(random.randint(1, 10))

# if the function import is used, you can call the function directly
print(randint(100, 150))

# if the function is imported universaly, you do not need to use the module name
print(random())