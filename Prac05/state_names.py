"""
CP1404 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        max_length = max((len(state_code) for state_code in CODE_TO_NAME))
        print("{:{}} is {}" .format(state_code, max_length, CODE_TO_NAME[state_code]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
