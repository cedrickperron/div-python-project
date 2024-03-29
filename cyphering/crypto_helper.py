
# The Global Variable representing the alphabet is defined
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
 
 
def in_engl_alpha(input_string):
    """
    (str) --> boolean
    This function transforms all the symbols of the non-empty input's string into their lowercase symbols. Then,
    this function determines if the lowercase input string contains only symbol from the english alphabet. It returns
    True if it does contain only symbols from the English alphabet, and False if it does not.
    >>> in_engl_alpha('c')
    True
    >>> in_engl_alpha('R')
    True
    >>> in_engl_alpha('doc')
    True
    >>> in_engl_alpha('apples and orange')
    False
    >>> in_engl_alpha('%')
    False
    >>> in_engl_alpha('7')
    False
    """
    # As the function must not be case-sensitive, the string is adjusted so that all its character are lowercase.
    lowercase_input_string = input_string.lower()
    # iterate through each character of the string and determine if they consist of symbol from the English alphabet
    for character in lowercase_input_string:
        if character not in ALPHABET:
            return False
    return True
def shift_char(input_string, position_to_left_of_input_string_in_the_alphabet):
    """
    (str, int) --> str
    The function encrypts an input_string into the letter in the alphabet corresponding to a position n later of the input_string.
    The position n later is an integer and it is the second input of the function. The first input is the input_string and it represents a string.
    At first, the function determines if the input_string consists of a single character and if not, the function raises a ValueError
    with the message: the input string should consist of only one character only. Otherwise, the string calls the function in_engl_alpha to determine
    if the character is from the English alphabet and if not; that is (if in_engl_alpha returns False), the function returns the character
    itself with no modification. If the function corresponds from a letter in the English alphabet, the function returns the
    lowercase letter which appear at n position later in the alphabet (the integer n is given by the second input).
    >>> shift_char('d', 25)
    'c'
    >>> shift_char('s', 5)
    'x'
    >>> shift_char('A', -2)
    'y'
    >>> shift_char('%', 5)
    '%'
    >>> shift_char('g', 500)
    'm'
    >>> shift_char('rat', 53)
    Traceback (most recent call last):
    ...
    ValueError: the input string should contain a single character
    """
    # This make sure that the input string consists of only one character
    if len(input_string) != 1:
        raise ValueError("The input string should contain a single character")
    else:
        is_character_from_english_alphabet = in_engl_alpha(input_string) # Determine if the input_string is from the English Alphabet
        if is_character_from_english_alphabet == True:
            lowercase_input_string = input_string.lower() # Change the input_string into a lower case
            index_of_input_string_in_alphabet = ALPHABET.find(lowercase_input_string) # Determine the position (index) of the input_string in the alphabet starting at a = 0, b = 1, ..., z = 25
            index_of_character_the_input_string_transforms_into = index_of_input_string_in_alphabet + position_to_left_of_input_string_in_the_alphabet # Find the character for which the input_string transforms into
            while (index_of_character_the_input_string_transforms_into > 25):
                index_of_character_the_input_string_transforms_into -= 26 # Adjust the index of the alphabet to make it such that the 26th index corresponds to a, 27th index correspond to b, ..., 51th index corresponds to z and so on.
            while (index_of_character_the_input_string_transforms_into < 0):
                index_of_character_the_input_string_transforms_into += 26 # Adjusts the index of the alphabet to make it such that the -1th index corresponds to z, -2th index corresponds to y, ... -26th index corresponds to a, and so on.
            return ALPHABET[index_of_character_the_input_string_transforms_into]
        else:
              return input_string
 
def get_keys(input_string):
    """
    (str) --> [int]
    The function indicates the position of all character of an input string (first input) in the alphabet
    (starting at a = position 0) provided that all the characters of the input string belongs to the English
    language. If the string is empty, then the function should return an empty list and if the string contains
    character not present in the English alphabet, a ValueError should be raised with the message: the input string
    must containt only characters from the English alphabet.
    >>> get_keys("good")
    [6, 14, 14, 3]
    >>> get_keys("NHL")
    [13, 7, 11]
    >>> get_keys('')
    []
    >>> get_keys('49')
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet.
    """
    lowercase_input_string = input_string.lower()  # We prevent the function from being case-sensitive by transforming all input string into their respective lowercase string
    in_english_alphabet = in_engl_alpha(lowercase_input_string)
    if in_english_alphabet == False:
        raise ValueError("the input string must contain only characters from the English alphabet.")
    else:
        list_of_index_of_character_of_the_input_string = [] # We create a new empty list in which we will add the index of each character of the input string using a for loop
        for character in lowercase_input_string:
            index_of_character_of_input_string_in_the_alphabet = ALPHABET.find(character)
            list_of_index_of_character_of_the_input_string += [index_of_character_of_input_string_in_the_alphabet]    
        return list_of_index_of_character_of_the_input_string
 
def pad_keyword(input_string, desired_length):
    """
    (str, int) --> str
    This function takes as input a string and an integer n indicating the desired length of the string. It returns
    a string of the length n by concatenating characters of the input string together until the desired length
    is met. If a string is empty, the function raises a ValueError with the message: the string must not be empty.
    >>> pad_keyword('Banana', 20)
    'BananaBananaBananaBa'
    >>> pad_keyword('school', 2)
    'sc'
    >>> pad_keyword('',5)
    Traceback (most recent call last):
    ValueError: the string must not be empty.
    """
    if input_string == '':
        raise ValueError("the string must not be empty")
    else:
        desired_string = "" # We create an empty string for which the characters of the input string will be added in order to give the desired length
        if desired_length <= len(input_string):
            desired_string = input_string[0:desired_length] # If the input string is longer than the desired length, we slice the string such that it includes all the character of the string starting from the first character (index = 0) until the character with the index of the desired length
        else:
            # while loop determining how many time the input string fit completely in the desired length.
            while desired_length >= len(input_string):
                desired_string += input_string
                desired_length -= len(input_string)
            # If the input string does not fit completely in the desired length, than the remain characters of the input string are added in such a manner that the first character added is the character corresponding to index 0
            if desired_length > 0:
                index = 0
                for index in range(desired_length):
                    desired_string += input_string[index]
        return desired_string
