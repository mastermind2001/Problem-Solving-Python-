# Date : 05-06-2018
# Reciprocal Letters

import string


# main function for reciprocal letters
def reciprocal(letter):
    """
    :param letter: a string
    :return: reciprocal of that string
    """
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase

    reciprocal_letter = ''

    for i in letter:
        if i in lower_case:
            index = lower_case.index(i)
            reciprocal_letter += lower_case[::-1][index]
        elif i in upper_case:
            index = upper_case.index(i)
            reciprocal_letter += upper_case[::-1][index]
        else:
            reciprocal_letter += ' '

    return reciprocal_letter


flag = True

strings = string.ascii_letters+' '

# input a string
letters = input()

for a in letters:
    if a not in strings:
        flag = False
        break

# error handling for wrong input
if flag:
    # calling function reciprocal()
    print(reciprocal(letters))
else:
    print('Invalid Input. You can enter only string.')

