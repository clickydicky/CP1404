# Q1
name = input('Enter your name: ')
my_file = open('name.txt', 'w')
print('Your name is {}' .format(name), file=my_file)
my_file.close()

# Q2
my_file = open('name.txt')
for line in my_file:
    print(line)
my_file.close()

# Q3
numbers_file = open('numbers.txt', 'w')
numbers_file.write('17\n')
numbers_file.write('42\n')
numbers_file.write('100\n')
numbers_file.close()

numbers_file = open('numbers.txt', 'r')

total = 0
for i in range(2):
    line = numbers_file.readline()
    total = total + int(line)
print(total)

# Q4
lines = numbers_file.readlines()
total = 0
for line in lines:
    for i in line:
        total = total + int(line)
print(total)
numbers_file.close()
