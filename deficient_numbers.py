# Date : 24-05-2018
# Deficient Numbers


# main function for telling a number is deficient or not
def is_deficient(num):
    """
    :param num: a positive integer value
    :return: a string indicating a number is deficient or not
    """
    store_sum = 0
    # iterate over an entire range, range = num+1
    for integer in range(1, num+1):
        if num % integer == 0:
            store_sum += integer

    if store_sum < 2*num:
        print(str(num) + " is a deficient number")
        print('\n---------------------------------\n')

    else:
        print(str(num) + " is not a deficient number")
        print('\n---------------------------------\n')


# copied First function for return different result (a boolean value)
def is_deficient_copy(num):
    """
    :param num: a positive integer value
    :return: a string indicating a number is deficient or not
    """
    store_sum = 0
    # iterate over an entire range, range = num+1
    for integer in range(1, num+1):
        if num % integer == 0:
            store_sum += integer

    if store_sum < 2*num:
        return True

    else:
        return False


# main function for printing deficient numbers up to a given range
def deficient_numbers_range(num):
    """
    :param num: a positive integer value
    :return: all deficient numbers up to a given range, range = input num
    """
    print('Deficient numbers up to ' + str(num) + ' are : \n')
    # iterate over an entire range, range = num+1
    for integer in range(1, num + 1):
        if is_deficient_copy(integer):
            print(integer)
    print('\n---------------------------------\n')


# main function for telling a number is deficient or not and displaying everything
def displaying_deficient(num):
    """
    :param num: a positive integer value
    :return: a string indicating a number is deficient or not
    """
    # storing factors as strings
    store_factors = ''
    store_sum = 0
    # iterate over an entire range, range = num+1
    for integer in range(1, num+1):
        if num % integer == 0:
            store_sum += integer
            store_factors += str(integer) + ', '
    print('Factors of '+str(num)+' are : '+store_factors[:-2]+'\n')
    print('Sum of factors is : '+str(store_sum)+'\n')

    if store_sum < 2*num:
        print(str(num) + " is a deficient number")
        print('\n---------------------------------\n')

    else:
        print(str(num) + " is not a deficient number")
        print('\n---------------------------------\n')


# input a positive integer value
number = input()

# error handling for wrong input
if number.isdigit():
    if int(number) > 0:
        # calling function is_deficient
        is_deficient(int(number))
        # calling function deficient_numbers_range
        deficient_numbers_range(int(number))
        # calling function displaying_deficient
        displaying_deficient(int(number))
    else:
        print('Invalid input. You can enter only positive integers')
else:
    print('Invalid input. You can enter only positive integers')

