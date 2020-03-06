# Date : 12-06-2018
# Word Frequency counter


# function for counting how many times a given word occur in a string
def count_string(string, word):
    """
    :param string: a sentence
    :param word: a letter that needs to be counted in that sentence
    :return: how many times that word occur in that sentence
    """
    count = string.lower().count(word.lower())
    a = '\n--------------------------------\n'
    return 'Number of times [ ' + word + ' ] present in [ ' + string + ' ] is : ' + a + str(count)


# input a sentence
text = input()

# input a word
word = input()

# calling function count_string()
print(count_string('{}'.format(text), '{}'.format(word)))

