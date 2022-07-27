MENU = "(E)ven\n(O)dd\n(S)quare\n(Q)uit"
x = int(input("Enter x number: "))
y = int(input("Enter y number: "))
while y < x:
    print("Invalid input")
    x = int(input("Enter x number: "))
    y = int(input("Enter y number: "))
print(MENU)
choice = input("Enter choice: ").upper()
if choice == "E":
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)
elif choice == "O":
    for i in range(x, y + 1):
        if i % 2 == 1:
            print(i)
elif choice == "S":
    for i in range(x, y + 1):
        print(i**2)
else:
    print("Finished")
