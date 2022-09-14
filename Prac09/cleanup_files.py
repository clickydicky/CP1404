"""
Cleanup inconsistent file names
"""

import os
import re


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a consistent naming of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt").replace("()([A-Z])", "_")\
        .replace('(?<=[a-z])(?=[A-Z0-9])', '_').replace('(?<=[(])', '_')
    return new_name


main()

