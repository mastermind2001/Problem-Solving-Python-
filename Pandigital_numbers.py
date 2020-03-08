# Date : 10-06-2018
# Pandigital Numbers

"""
If a number contains each of the
digits from 0 to 9 at least once (0
not being the leading digit), it is
considered to be pandigital
"""


# function returning number of times each digit appears in that number
def number_of_times(num):
    """
    :param num: a positive integer
    :return: nothing
    """
    print('Number of times each digit displayed in number is : \n')
    store = {}
    for i in range(10):
        if str(i) in num:
            store[i] = num.count(str(i))
        else:
            store[i] = '0'

    for keys in store.keys():
        print(str(keys) + '  ->  ' + str(store[keys]))


# function for checking pandigital number
def isPandigital(num):
    """
    :param num: a positive integer
    :return: whether num is Pandigital or not
    """
    flag = True

    if num[0] == '0':
        number_of_times(num)
        print('\n--------------------------------\n')
        return num + ' is not a Pandigital Number.'

    for i in range(10):
        if str(i) not in num:
            flag = False
            break

    if flag:
        number_of_times(num)
        print('\n--------------------------------\n')
        return num + ' is a Pandigital Number.'
    else:
        number_of_times(num)
        print('\n--------------------------------\n')
        return num + ' is not a Pandigital Number.'


# input a positive integer
number = input()

# error handling for wrong input
if number.isdigit():
    # calling function isPandigital()
    print(isPandigital(number))
else:
    print('Invalid input. You can enter only digits.')

