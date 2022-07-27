import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? a random integer being generated from the range (5, 20)
# What was the smallest number you could have seen, what was the largest? smallest will be 5 and largest will be 19.

# What did you see on line 2? a random number being generated from the range of (3, 10, 2)
# What was the smallest number you could have seen, what was the largest? smallest will be 3 and largest will be 9
# Could line 2 have produced a 4? no

# What did you see on line 3? a random floating number being generated from the range of (2.5, 5.5)
# What was the smallest number you could have seen, what was the largest? smallest will be 2.5 and largest will be 5.5

print(random.randint(1, 100))
