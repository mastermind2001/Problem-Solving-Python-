# Date : 06-06-2018
# Automorphic Numbers

"""
If the square of a number ends with
the number itself, it is considered to
be automorphic.
"""


# function for checking whether a number is automorphic or not
def is_automorphic(num):
    """
    :param num: a positive integer value
    :return: whether it is automorphic or not
    """
    num_sqr = num * num

    if str(num) == str(num_sqr)[-len(str(num)):]:
        return str(num) + ' is an automorphic number.'
    else:
        return str(num) + ' is not an automorphic number.'


# function for finding all automorphic numbers up to a range
def automorphic_range(num):
    """
    :param num: a positive integer value
    :return: all automorphic numbers up to num
    """
    print('\n--------------------------------\n')
    print('Automorphic numbers upto '+str(num)+' are : \n')

    for i in range(1, num+1):
        if str(i) == str(i * i)[-len(str(i)):]:
            print(i)


# input a positive integer value
number = input()

if number.isdigit():
    if int(number) > 0:
        # calling function is_automorphic()
        print(is_automorphic(int(number)))

        # calling function automorphic_range()
        automorphic_range(int(number))
    else:
        print('Invalid input. You can enter only positive integers.')
else:
    print('Invalid input. You can enter only positive integers.')

