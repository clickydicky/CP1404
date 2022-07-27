print("Loop 1:")
for i in range(0, 101, 10):
    print(i)
print("Loop 2:")
for i in range(20, 0, -1):
    print(i)
stars = int(input("Enter number of stars: "))
print("Loop 3:")
for i in range(1, stars):
    print('*', end='')
print("Loop 4:")
for i in range(1, stars + 1):
    print('*' * i)
