import random
import string
print('Password Generator Initialized')
how_long = input('How many charecters long?')
print("".join(random.choices(string.ascii_letters + string.digits, k=int(how_long))))