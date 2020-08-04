import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet=set(alphabet)
    str1=set(str1.replace' ', '')
    return alphabet==str1