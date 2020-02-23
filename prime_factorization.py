# Date : 03-06-2018
# Prime Factorization

# input a positive integer greater than 1
number = input()

# storing the original value of number
number_copy = number


# main function for prime factorization
def prime_factorization(num):
    """
    :param num: a positive integer
    :return: prime factorization
    """
    # factors of num
    index = 2

    # store prime factors
    store_prime = ''

    # iterate until num decreases to 1
    while num > 1:
        power = 0
        # iterate until index is a factor of num
        while num % index == 0:
            # increment the power by 1 each time when the index is a factor of num
            power += 1
            # decrease num each time by the factor of num (i.e index)
            num //= index
        # check if we find a factor of num
        if power != 0:
            store_prime += str(index) + '^' + str(power) + ' * '
        # increment the index each time by 1
        index += 1
        
    return str(number_copy) + ' = ' + store_prime[:-3]


# error handling for wrong input
if number.isdigit():
    if int(number) > 1:
        # calling function prime_factorization
        print(prime_factorization(int(number)))
    else:
        print('Invalid Input. You can enter only positive integer greater than 1.')
else:
    print('Invalid Input. You can enter only positive integer greater than 1.')

