# Date : 31-05-2018
# Is that an IP Address?

import re


# main function for checking valid or invalid IP Address
def isValidIPAddress(ip_address):
    """
    :param ip_address: an IP address
    :return: whether IP address is valid or not
    """
    flag = True
    # pattern of IP Address
    pattern = r'^(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}$'

    # match the input IP Address to the pattern
    match = re.match(pattern, ip_address)

    # check if IP Address is valid or not
    if match:
        ip_address_list = match.group().split('.')
        for i in ip_address_list:
            if int(i) > 255 or int(i) < 0:
                 flag = False
        if flag:
            return 'IP Address is Valid'
        else:
            return 'IP Address is Invalid'
    else:
        return 'IP Address is Invalid'


# input the IP Address
ip_address = input()

# calling function isValidIPAddress()
print(isValidIPAddress(ip_address))

