"""Get a password of a minimum length and display asterisks"""
MINIMUM_LENGTH = 5


def main():
    """Get a password and print asterisks"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get a password and ensure it meets the minimum_length requirement."""
    password = input("Enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid. Password must be at least {} characters.".format(MINIMUM_LENGTH))
        password = input("Enter your password: ")
    return password


def print_asterisks(characters):
    """Print the length of characters in asterisks."""
    print('*' * len(characters))


main()
