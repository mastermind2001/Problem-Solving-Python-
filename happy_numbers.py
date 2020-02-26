# Date : 25-05-2018
# Happy Numbers

# input a positive integer value
number = input()

# store original number
num_store = number


# main function for telling whether a number is happy or not
def happy_numbers(num):
    """
    :param num: a positive integer value
    :return: a string indicating whether the input number is happy or not
    """
    if num == 1:
        print(num_store + ' is a happy number.')
        print('\n------------------------------\n')

    while num != 1:
        num_lst = list(str(num))
        num = 0
        for i in num_lst:
            num += int(i)**2

        if num == 1:
            print(num_store+' is a happy number.')
            print('\n------------------------------\n')
            break

        if num == 4:
            print(num_store+' is not a happy number.')
            print('\n------------------------------\n')
            break


# function happy_numbers copy
def happy_numbers_copy(num):
    """
    :param num: a positive integer value
    :return: a string indicating whether the input number is happy or not
    """
    if num == 1:
        return True

    while num != 1:
        num_lst = list(str(num))
        num = 0
        for i in num_lst:
            num += int(i)**2

        if num == 1:
            return True

        if num == 4:
            return False

# main function for printing all happy numbers up to a given range
def happy_numbers_range(num):
    """
    :param num: a positive integer value
    :return: all happy numbers up to a given range, range = input number
    """
    print('Happy numbers up to '+num_store+' are : \n')
    for i in range(1, num+1):
        if happy_numbers_copy(i):
            print(i)
    print('\n------------------------------\n')


# main function for displaying every sum of squares operation
def happy_numbers_display(num):
    """
    :param num: a positive integer value
    :return: display all operations
    """
    store = ''
    print('Operations : \n')
    if num == 1:
        print('1^2 = '+str(num))
        print('\n'+num_store + ' is a happy number.')
        print('\n------------------------------\n')

    while num != 1:
        num_lst = list(str(num))
        num = 0

        for i in num_lst:
            num += int(i)**2

        for i in num_lst:
            store += i+'^2 + '
        print(store[:-2]+'= '+str(num))
        store = ''

        if num == 1:
            print('\n'+num_store+' is a happy number.')
            print('\n------------------------------\n')
            break

        if num == 4:
            print('\n'+num_store+' is not a happy number.')
            print('\n------------------------------\n')
            break


# error handling for wrong input
if number.isdigit():
    if int(number) > 0:
        # calling function happy_numbers
        happy_numbers(int(number))
        # calling function happy_numbers_range
        happy_numbers_range(int(number))
        # calling function happy_numbers_display
        happy_numbers_display(int(number))
    else:
        print('Invalid input. You can enter only positive integers.')
else:
    print('Invalid input. You can enter only positive integers.')

