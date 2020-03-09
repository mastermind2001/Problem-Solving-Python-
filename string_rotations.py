# Date : 28-07-2018
# String Rotations


def string_rotations(text):
    """
    :param text: a string
    :return: list of rotated strings
    """
    rotated_strings = []

    for i in range(len(text)):
        rotated_strings.append(text[i+1:] + text[:i+1])

    return rotated_strings


# calling function string_rotations
print(string_rotations(input()))

