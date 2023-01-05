'''
Random Numbers
1/5/2023
Python I

Instructions:
Run the program several times to see how it
generates random numbers. Once you understand
how the program works, modify it to display a
random number between 100 and 200, inclusive.
'''

import random

print(random.randint(1, 6))
print(random.randint(1, 2))
print(random.randint(0, 1))
print(random.randint(1, 12))
print(random.randint(1, 20))
print(random.random())

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
total = roll1 + roll2
print("Move " + str(total) + " spaces!")