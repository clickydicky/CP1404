"""Get a password of a minimum length and display asterisks"""
MINIMUM_LENGTH = 5


def main():
    """Get a password of a minimum length and print asterisks"""
    password = input("Enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid. Password must be at least {} characters.".format(MINIMUM_LENGTH))
        password = input("Enter your password: ")
    print('*' * len(password))


main()
