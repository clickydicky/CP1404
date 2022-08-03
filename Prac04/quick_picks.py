import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Randomly choose 6 numbers per row and display it"""
    number_of_quick_picks = int(input("Enter number of quick picks you want: "))
    while number_of_quick_picks < 0:
        print("Invalid input. Please enter an integer.")
        number_of_quick_picks = int(input("Enter number of quick picks you want: "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for num in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
