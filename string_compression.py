# Date : 02-06-2018
# String Compression

import re


# main function for string compression
def string_compression(string):
    """
    :param string: a string
    :return: compressed string
    """
    # compressed string
    new_string = ''

    while len(string) != 0:
        new_string += string[0] + str(string.count(string[0]))
        string = re.sub(string[0], '', string)

    return new_string


# input a string
letters = input()

# format for input
pattern = r'^[A-Za-z]+$'

# check whether input string match the format
match = re.match(pattern, letters)

# error handling for wrong input
if match:
    # calling function string_compression()
    print(string_compression(letters))
else:
    print('Invalid Input. You can enter only letters.')

