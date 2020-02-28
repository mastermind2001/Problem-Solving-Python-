
# Cube root
"""
A cube root of a number x is a
y such that y*y*y = x.
Example: 2 * 2 * 2 = 8, so the cube
root of 8 is 2.
"""

"""
Algorithm used to find cube root
is a famous one name:
 
Newton - Raphson method.

For finding the cube root of a number
say 27 :

For a polynomial P(x) such that:

P(x) = x^3 - 27

Then we need to find the value of
x for which the value of P(x) = 0
and that is the cube root of 27.

Newton - Raphson method states
that if you have a good guess for value of
x takes then you can make it 
a better guess with Newton - Raphson method.

For eg:

P(x) = x^3 -27

if g is a good guess for value of x.
Then you can make it better guess with
Newton - Raphson formula.

P(g) = g^3 - 27

where g changes as : 

g = g - ( p(g) / p'(g) )

where,

g = guess
p(g) = polynomial with respect to g
p'(g) = derivative of polynomial with respect to g
"""


def cube_root(num):
    """
    :param num: a positive integer value
    :return: cube root of num
    """
    epsilon = 0.0001
    guess = num

    while (guess**3 - num) > epsilon:

        guess = guess - (((guess**3) - num) / (3 * (guess**2)))

    design = '\n\n------------------------------------\n\n'
    return 'Cube root of ' + str(num) + ' is : ' + design + str(round(guess, 4))


# input a positive integer value
number = input()

# error handling for wrong input
if number.isdigit():
    # calling function cube_root()
    print(cube_root(int(number)))
else:
    print('Invalid input. You can enter only positive integers.')

