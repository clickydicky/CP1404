"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the user gives an invalid input but is considered as a valid argument
2. When will a ZeroDivisionError occur? When the user enters the denominator input as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, shown below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
