# Date : 05-06-2018
# LCM and HCF

# input example
# Step 1. Input a number indicating that of how many numbers you want to compute lcm and hcf
# Step 2. Press enter to enter a new line and enter the numbers for lcm and hcf
# Step 3. At last press submit

# Step 1.  4
# Step 2.  2
#          4
#          6
#          8
# Step 3. Press Submit

# Output :
# LCM of [2, 4, 6, 8] is : 24
# HCF of [2, 4, 6, 8] is : 2

# list of number for lcm and hcf
store_num = []


# function for input
def num_input(num):
    """
    :param num: a positive integer value and indicates quantity of numbers you want to find lcm and hcf
    :return: nothing
    """
    for i in range(num):
        try:
            nums = int(input())
            if nums > 0:
                store_num.append(nums)
            else:
                break
        except ValueError:
            break


# main function for finding LCM
def lcm():
    """
    :return: lcm of numbers
    """
    # list of numbers for lcm
    lcm_nums = store_num

    # maximum number in lcm_nums
    max_num = max(lcm_nums)

    max_num_copy = max_num

    flag = True

    while flag:
        for i in lcm_nums:
            if max_num % i != 0:
                max_num += max_num_copy
                break
        else:
            flag = False

    return 'LCM of '+str([i for i in lcm_nums])+' is : '+str(max_num)


def hcf():
    """
    :return: hcf of numbers
    """
    # list of numbers for hcf
    hcf_nums = store_num

    # minimum number in hcf_nums
    least_num = min(hcf_nums)

    flag = True

    while flag:
        for i in hcf_nums:
            if i % least_num != 0:
                least_num -= 1
                break
        else:
            flag = False

    print('\n-----------------------------------\n')

    return 'HCF of '+str([i for i in hcf_nums])+' is : '+str(least_num)


# input a positive number
number = input()

# error handling for wrong input
if number.isdigit():
    if int(number) > 0:
        # calling function num_input()
        num_input(int(number))
        if len(store_num) == int(number):
            # calling function lcm()
            print(lcm())
            # calling function hcf()
            print(hcf())
        else:
            print('Invalid input. You can enter only positive integers.')
    else:
        print('Invalid input. You can enter only positive integers.')
else:
    print('Invalid input. You can enter only positive integers.')

