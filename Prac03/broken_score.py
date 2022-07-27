"""
CP1404/CP5632 - Practical
Broken program to determine score status, with functions
"""


def main():
    """Get numeric score and print its status"""
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    """Determine the result of a score"""
    if 0 > score > 100:
        print("Invalid score")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


main()
