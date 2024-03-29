# dict_utils.py
def count_occurrences(input_word):
    """
    (str) --> dict
    Takes as input a string and returns a dictionary mapping each
    characters of the string (key) to an integer corresponding to
    the number of occurrences of each character in the string
    >>> d = count_occurrences('canada')
    >>> d == {'c': 1, 'a': 3, 'n': 1, 'd': 1}
    True
    >>> d = count_occurrences('pear')
    >>> d == {'p': 1, 'e': 1, 'a': 1, 'r': 1}
    True
    >>> d = count_occurrences('banana')
    >>> d == {'b':1, 'a':3, 'n':2}
    True
    """
    # Create a dictionary that will count each letter in the input word
    letter_counting_dict = dict()
    # Iterate through each letter of the input word
    for letter in input_word:
        if letter in letter_counting_dict:
            letter_counting_dict[letter] += 1
        else:
            letter_counting_dict[letter] = 1
    return letter_counting_dict
 
def flatten_dict(input_dict):
    """
    (dict) --> list
    Takes as input a dictionary with string as key and non-negative integer as
    value and return a list containing the key string appearing as many time as the value
    associated to it. The input dictionary should not be modified.
    >>> d = {'p': 1, 'e': 1, 'a': 1, 'r': 1}
    >>> a = flatten_dict(d)
    >>> a.sort()
    >>> a == ['a', 'e', 'p', 'r']
    True
    >>> d == {'p': 1, 'e': 1, 'a': 1, 'r': 1}
    True
    
    >>> d = {'sort': 2, 'count': 1, 'remove': 1}
    >>> a = flatten_dict(d)
    >>> a.sort()
    >>> a == ['count', 'remove', 'sort', 'sort']
    True
    >>> d == {'sort': 2, 'count': 1, 'remove': 1}
    True
    >>> d = {'let': 2, 'it': 2, 'be': 3}
    >>> a = flatten_dict(d)
    >>> a.sort()
    >>> a == ['be', 'be', 'be', 'it', 'it', 'let', 'let']
    True
    >>> d == {'let': 2, 'it': 2, 'be': 3}
    True
    """
    # Create an empty list of characters
    list_of_char = []
    # Iterate through each characters and the amount at which they are present  
    for char, amount  in input_dict.items():
        for i in range(amount):
            list_of_char.append(char)
    return list_of_char
 
def get_word_score(input_word, point_worth_of_letter):
    """
    (str, dict) --> int
    Take as input a string representing a word as well as a dictionary
    that maps each character to the appropriate points that the character is worth
    The function returns the total point of the word. If a character of the word is not
    in the dictionary, then it is worth zero point.
    >>> p = {'a': 3, 's': 1, 't': 2, 'r': 4, 'i': -2, 'n': 8}
    >>> get_word_score('stain', p)
    12
    >>> p = {'a': 3, 's': 1, 't': 2, 'r': 4, 'i': -2, 'n': 8}
    >>> get_word_score('train', p)
    15
    >>> p = {}
    >>> get_word_score('train', p)
    0
    >>> p = {'a': 3, 's': 1, 't': 2, 'r': 4, 'i': -2, 'n': 8}
    >>> get_word_score('refrain', p)
    17
    >>> p = {}
    >>> get_word_score('train', p)
    0
    >>> p = {'a': 3, 's': 1, 't': 2, 'r': 4, 'i': -2, 'n': 8}
    >>> get_word_score('', p)
    0
    """
    word_total_point = 0 # Set the total point of the word to zero
    # Iterate through the letters of the chosen word
    for letter in input_word:
        # Add the point worth of the letter to the total point of the word
        if letter in point_worth_of_letter:
            word_total_point += point_worth_of_letter[letter]
    return word_total_point
 
def is_subset(subset_dict, larger_dict):
    """
    (dict, dict) --> bool
    Takes as input two dictionaries with letters as key and the point associated to those letters
    and returns a boolean value indicating the first dictionary is a subset of the second. To be a subset,
    all the keys of the first dictionaries must be in the larger dictionaries and the values associated to those
    keys must be smaller or equal in the first dictionary. The function should not modify the input dictionary.
    Furthe, the values assiociated to each dictionary are assumed to be positive.
    
    >>> d_one = {'a': 3, 's': 1, 't': 2}
    >>> d_two = {'a': 4, 's': 1, 't': 5, 'r': 3, 'd': 5}
    >>> d_three = {'a': 4, 's': 1, 't': 4, 'r': 1, 'd': 5}
    >>> is_subset(d_one, d_two)
    True
    >>> is_subset(d_one, d_three)
    True
    >>> is_subset(d_three, d_two)
    True
    >>> is_subset(d_two, d_three)
    False
    >>> is_subset(d_three, d_one)
    False
    """
    # Iterate through letters of subset_dict
    for letter in subset_dict:
        # Check if the same letter are present in the larger_dict (return False if not)
        if (letter not in larger_dict):
            return False
        # Check if for all letters present in both dictionaries, a greater or equal amount of each letter is present in larger_dict (return False if not)
        if ((subset_dict[letter]) > (larger_dict[letter])):
            return False
    return True
 
def subtract_dicts(larger_dict, subset_dict):
    """
    (dict, dict) --> bool
    Takes as input a larger dictionary and a subset dictionary and return a boolean value
    mentionning if the subset dictionary is a subset of the larger dictionary (True) or not (False).
    Provided that it is a subset, the function then updates the values of the key of the larger dictionary by substracting the initial values of its key
    by those of the subset dictionary. If the value of the key of the uptaded dictionary is zero, the key is removed.
    If the subset dictionary is not a subset of the larger, then no change occurs.
    
    >>> d_one = {'a': 3, 's': 1, 't': 2}
    >>> d_two = {'a': 4, 's': 1, 't': 5, 'r': 3, 'd': 5}
    >>> d_three = {'a': 4, 's': 1, 't': 4, 'r': 1, 'd': 5}
    >>> subtract_dicts(d_two, d_one)
    True
    >>> d_two == {'a': 1, 't': 3, 'r': 3, 'd': 5}
    True
    >>> subtract_dicts(d_three, d_two)
    False
    >>> d_three == {'a': 4, 's': 1, 't': 4, 'r': 1, 'd': 5}
    True
    >>> subtract_dicts(d_three, d_one)
    True
    >>> d_three = {'a': 1, 't': 2, 'r': 1, 'd': 5}
    >>> subtract_dicts(d_two, d_three)
    True
    >>> d_two == {'t': 1, 'r': 2}
    True
    """
    # If subset dict is a subset of larger dict, then the dictionary is changed
    if is_subset(subset_dict, larger_dict):
        # Iterate through the letters of the subset dict
        for letter in subset_dict:
            # Removing the letters of subset dict from larger_dict
            larger_dict[letter] -= subset_dict[letter]
            # If the letters are not present anymore, they are removed from larger_dict
            if larger_dict[letter] == 0:
                larger_dict.pop(letter)
                
        return True
    
    else:
        return False
 
def create_scrabble_dict(list_of_words):
    """
    (list) --> dict
    Takes as input a list containing words and returns a dictionary that maps
    integers representing the number of character in the word (as key) and a dictionary
    that maps the first letter of the words (as key) to the words themselves as list of string (as value).
    
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(w)
    >>> d == {2 : {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3 : {'c': ['cat', 'can', 'cow'], 'd': ['dog', 'dad']}, 5 : {'h': ['hippo'], 'u' : ['umami', 'uncle'] }}
    True
    >>> w = ['ant', 'apple', 'bar', 'barns', 'car', 'cabin']
    >>> d = create_scrabble_dict(w)
    >>> d == {3: {'a': ['ant'], 'b': ['bar'], 'c': ['car']}, 5: {'a': ['apple'], 'b': ['barns'], 'c': ['cabin'] }}
    True
    >>> w = ['sage', 'saga', 'safe', 'cafe', 'cabs','cool']
    >>> d = create_scrabble_dict(w)
    >>> d == {4: {'s': ['sage', 'saga', 'safe'], 'c': ['cafe', 'cabs', 'cool']}} 
    True
    """
    # Create the dictionary mapping each words to their length (key of dictionary)
    dict_map_length_of_words = dict()
    
    # Iterating through each word of the list of words (input)
    for word in list_of_words:
        # Associating each word to the key corresponding to its length. The length will map to a list containing all the words with this length
        if len(word) in dict_map_length_of_words:
            dict_map_length_of_words[len(word)] += [word]
        else:
            dict_map_length_of_words[len(word)] = [word]
    # Iterating through the length of the words (key) and the list of words with this length (value).
    for length_of_word, word_list_with_same_length in dict_map_length_of_words.items():
        # Create a dictionary that will take the list of words with the same length and maps them according to their starting letter
        sub_dict_map_words_with_same_first_char = dict()
        # Iterating through each word with the same length in the list
        for word in word_list_with_same_length:
            # Associating each word to the key corresponding to their starting letter. The value will be a list of words with same length and starting letters
            if word[0] in sub_dict_map_words_with_same_first_char:
                sub_dict_map_words_with_same_first_char[word[0]] += [word]
            else:
                sub_dict_map_words_with_same_first_char[word[0]] = [word]
        # Associating each length of word (key) to the dictionary mapping the word of the same length to their starting letter
        dict_map_length_of_words[length_of_word] = sub_dict_map_words_with_same_first_char   
    
    return dict_map_length_of_words
 
def is_valid_word(word, valid_words_dict):
    """
    (str, dict) --> bool
    Takes as input a word and a dictionary of the same
    format as the one returned by the function create_scrabble_dict. The
    function returns whether the word appeared in the dictionary (True) or not (False)
    >>> w = ['sage', 'saga', 'safe', 'cafe', 'cabs','cool']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word('sage', d)
    True
    >>> is_valid_word('apple', d)
    False
    >>> is_valid_word('cab', d)
    False
    """
    # Check if there exists some valid words with same length as word inputed. Return False if not
    if len(word) not in valid_words_dict:
        return False
    else:
        # Dictionary containing all the valid words with the same length as the word inputed mapped to their starting letter
        dict_of_valid_words_with_same_length = valid_words_dict[len(word)]
        # Check if there exists some valid words with same length and starting letter. Return False if not
        if word[0] not in dict_of_valid_words_with_same_length:
            return False
        else:
            # Check if the input word is present in the list of valid words with same length and starting letters. Return False if not
            if word not in dict_of_valid_words_with_same_length[word[0]]: 
                return False 
    return True