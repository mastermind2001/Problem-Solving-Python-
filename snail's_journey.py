# Date : 23-06-2018
# A Snail's Journey

# Each day snail climbs up A meters on a tree with H meters in height.
# At night it goes down B meters.
# Program which takes 3 inputs: H, A, B, and calculates how many days it will take 
# for the snail to get to the top of the tree.

# Input format :
# 15   # For H
# 1    # For A
# 0.5  # For B
#
# where H > A > B
import math

def snail_journey(height_of_tree, climbs_up, climbs_down):
    """
    :param height_of_tree: Height of tree
    :param climbs_up: snail climbs up A meters each day on a tree
    :param climbs_down: snail climbs down B meters each night from a tree
    :return: number of days it takes to climb tree
    """
    days = (height_of_tree - climbs_down) / (climbs_up - climbs_down)

    return 'Snail will take ' + str(math.ceil(days)) + ' days to climb the tree.'


# input positive integer values
H = input()
A = input()
B = input()

# error handling for wrong input
try:
    if float(H) and float(A) and float(B):
        H = float(H)
        A = float(A)
        B = float(B)

    if H > A > B:
        # calling function snail_journey
        print(snail_journey(H, A, B))

    else:
        raise ValueError

except ValueError:
    print("""Invalid input. You can enter only positive numbers.\n
Input format :\n
15   # For H
1    # For A
0.5  # For B

where H > A > B.""")

