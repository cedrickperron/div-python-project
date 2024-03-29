# cipher.py
import crypto_helpers
from crypto_helpers import *
def caesar(input_string, key, mode):
    """
    This function takes a string as input representing the message, an integer (k) representing the key
    of the cipher and another integer (m) representing the mode (encryption/decryption). If m = 1, the
    message will be encrypted, if m = -1, the message is decrypted. If m has any other value, a ValueError is raised
    indicating that no other mode is supported. If the mode is 1, each character of the input_string are transformed into
    their corresponding encrypted character in the alphabet  located at n position to their right (n is equal to the value of the key). If the mode
    is -1, each character of the input string are transformed to their corresponding to their decrypted character located at n position to their left
    in the alphabet (in this case, n is equal to the negative of the string).
    >>> caesar('werty', 23, 1)
    'tboqv'
    >>> caesar('wtaad', 15, -1)
    'hello'
    >>> caesar('shdof', 15, -1)
    'dsozq'
    >>> caesar('orange and apples', 6, 1)
    'uxgtmk gtj gvvrky'
    >>> caesar('good', 11, 5)
    Traceback (most recent call last):
    ...
    ValueError: mode not supported
    """
    message = '' # We create an empty string that correspond to the string that will be returned after the input string is encrypted or decrypted
    if mode == 1:
        # We iterate through each character of the input string and transforms each character into their corresponding encrypted character.
        for character in input_string:
            encrypted_character = shift_char(character, key)
            message += encrypted_character
    elif mode == -1:
        adjusted_key = -1*key # The decrypted character are located to the left of their respective encrypted character, thus we must adjust the key, such that the index of the decrypted character is smaller than that of the encrypted character
        # We iterate through each encrypted character and find the decrypted character at n position (where n is equal to the key) to left of the encrypted character
        for character in input_string:
            decrypted_character = shift_char(character, adjusted_key)
            message += decrypted_character
    else:
        raise ValueError("mode not supported")
    return message
        
def vigenere(input_string, key, mode):
    """
    This function takes a string as input representing the message, a string representing the key
    of the cipher and another integer (m) representing the mode (encryption/decryption). If m = 1, the
    message will be encrypted, if m = -1, the message is decrypted. If m has any other value, a ValueError is raised
    indicating that no other mode is supported. It returns a string representing the encrypted/decrypted message depending on the mode that
    was selected.
    >>> vigenere('HaPPy', 'good', 1)
    'nodse
    >>> vigenere('nodse', 'good', -1)
    'happy'
    >>> vigenere('apple and orange', 'fries', 1)
    'fgxpw rvh tiiryj'
    >>> vigenere('fgxpw rvh tiiryj', 'FRIES', -1)
    'apple and orange'
    >>> vigenere('HAPPY', 'Friend', 5)
    Traceback (most recent call last):
    ValueError: mode not supported
    """
    message = "" # We create an empty string that correspond to the string that will be returned after the input string is encrypted or decrypted
    desired_length_of_key = len(input_string) # We determine the length with which we must concatenating the keyword such that it has the same length as the input string
    if mode == 1: 
        adjusted_keyword = pad_keyword(key, desired_length_of_key)
        list_of_keys = get_keys(adjusted_keyword) 
        # We iterate through each decrypted character and find the encrypted character at n position (where n is equal to the key of the corresponding index) to right of the encrypted character
        index_of_keys = 0 # We set the index of the list  
        for character in input_string:
            encrypted_char = shift_char(character, list_of_keys[index_of_keys])
            message += encrypted_char
            index_of_keys += 1
    elif mode == -1:
        adjusted_keyword = pad_keyword(key, desired_length_of_key)
        list_of_keys = get_keys(adjusted_keyword)
        adjusted_list_of_keys = []
        # The decrypted character are located to the left of their respective encrypted character, thus we must adjust the keys, such that the decrypted character is to the left of the encrypted character
        # We change the value of the keys into their negative value, such that they will find the character at a position n to the left of the input string character 
        for position_of_keyword_char in list_of_keys:
            adjusted_keys = -1*position_of_keyword_char
            adjusted_list_of_keys += [adjusted_keys]
        index_of_keys = 0 # We set the index of the list of the position of each character of the keyword in the alphabet at zero, such that the position of the first character of the keyword in the alphabet will only affect the first character of the input string and so on.
        # We iterate through each encrypted character and find the decrypted character at n position (where n is equal to the adjusted key of the corresponding index) to left of the encrypted character
        for character in input_string:
            desired_char = shift_char(character, adjusted_list_of_keys[index_of_keys])
            message += desired_char
            index_of_keys += 1
    else:
        raise ValueError("mode not supported")
    return message 