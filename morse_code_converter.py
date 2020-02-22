# Date : 06-06-2018
# Morse code converter

"""
Morse code is a method of
transmitting text information as a
series of on-off tones, lights, or
clicks.
Each letter or numeral is
represented by a unique sequence
of dots and dashes.
"""

import string

# stores the code for every letter
morse_dict = {}


# function for creating morse_dict
def morse_dict_creator():
    """
    :return: nothing
    """
    # morse code for alphabets
    morse_code_alphabets = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                            '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-',
                            '.--', '-..-', '-.--', '--..']

    # morse code for numbers
    morse_code_numbers = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..',
                          '----.']

    # adding morse code for lower-case alphabets to morse_dict
    for letter in range(len(string.ascii_lowercase)):
        morse_dict[string.ascii_lowercase[letter]] = morse_code_alphabets[letter]

    # adding morse code for upper-case alphabets to morse_dict
    for letter in range(len(string.ascii_uppercase)):
        morse_dict[string.ascii_uppercase[letter]] = morse_code_alphabets[letter]

    # adding morse code for numbers to morse_dict
    for number in range(len(morse_code_numbers)):
        morse_dict[str(number)] = morse_code_numbers[number]


# function for converting string to morse code
def morse_code_converter(strings):
    """
    :param strings: a string contains alphabets and numbers
    :return: morse code of that string
    """
    # for storing morse code value of every input string
    new_string = ''

    # conversion of input string to morse code
    for letter in strings:
        if letter in morse_dict.keys():
            new_string += morse_dict[letter]
        else:
            new_string += letter
    
    print('Morse code for ('+strings+') is : \n')

    return new_string


# input a string
letters = input()

# calling function morse_dict_creator()
morse_dict_creator()

# calling function morse_code_converter()
print(morse_code_converter(letters))

