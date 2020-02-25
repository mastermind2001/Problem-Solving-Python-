# Date : 23-06-2018
# Floyd's Triangle


def floyd_triangle(num):
    """
    :param num: a positive integer value
    :return: number of rows = num in floyd's triangle
    """
    a = 1
    print('Floyd\'s Triangle : ')
    print('\n==============================\n')
    for i in range(1, num+1):
        for j in range(i):
            print(a, end=' ')
            a += 1
        print()

    a -= 1
    print('\n==============================\n')
    print('Reverse Floyd\'s Triangle : ')
    print('\n==============================\n')
    for n in range(num, 0, -1):
        for j in range(n, 0, -1):
            print(a, end=' ')
            a -= 1
        print()


# input a positive integer
number = input()

# error handling for wrong input
if number.isdigit():
    if int(number) > 0:
        # calling function floyd_triangle()
        floyd_triangle(int(number))
    else:
        print('Invalid input. You can enter only positive integers greater than 0.')
else:
    print('Invalid input. You can enter only positive integers greater than 0.')

