# scrabble_utils.py
import dicts_utils, board_utils, random # for random choice
 
def display_rack(rack):
    """
    (dict) --> NoneType
    Takes as input a dictionary representing the rack of a player. The
    function displays all the letters present in the rack in upper case in one
    line one
    >>> display_rack({'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 1})
    A B B E K S T 
    >>> display_rack({'a': 2, 'f': 1, 'g': 2, 'o': 1, 'z': 1})
    A A F G G O Z 
    >>> display_rack({'a': 2, 'e': 1, 't':1})
    A A E T 
    >>> display_rack({'a':1, 'r': 1, 't':1})
    A R T 
    """
    
    list_of_letter_in_rack = dicts_utils.flatten_dict(rack) # Transform the rack dictionary into a string dictionary
    # Iterate through all the letters of the rack
    for letter in list_of_letter_in_rack:
        print(letter.upper(), end = ' ')
 
def has_letters(rack, desired_word):
    """
    (dict, str) --> bool
    Takes as input a dictionary representing the rack of the player and a string
    representing the desired_word to play. The function returns if the word can be inserted;
    that is if all the characters in the input string are available on the rack, as True or cannot
    be inserted as False. If true, the function removes the characters used to play the word from
    the rack
    >>> r = {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 1}
    >>> has_letters(r, 'basket')
    True
    >>> r == {'b': 1}
    True
    >>> r = {'a': 2, 'f': 1, 'g': 2, 'o': 1, 'z': 1}
    >>> has_letters(r, 'ago')
    True
    >>> r == {'a': 1, 'f': 1, 'g': 1, 'z': 1}
    True
    >>> r = {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 1}
    >>> has_letters(r, 'cat')
    False
    >>> r == {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 1}
    True
    """
    # Creating a dictionary that map all the letters of the desired_word to the amount of time they appear in the word
    dict_of_letters_of_desired_word = dicts_utils.count_occurrences(desired_word)
    # Check if all letters of the word are in the rack and if so, substract those letters from rack
    return dicts_utils.subtract_dicts(rack, dict_of_letters_of_desired_word)
    
def refill_rack(rack, pool_of_letters, number_of_letters_desired_on_rack):
    """
    (dict, dict, int) --> NoneType
    Takes as input a dictionary representing the rack of the player, another dictionary
    representing the pool of letters and a positive integer representing the number of letter
    to be added onto the rack (provided that the pool has at least n letter). If the pool has less
    than n letters, than all the letters of the pool are picked. The function does not return any value,
    but modify the dictionaries representing the rack and pool of letter accordingly.
    >>> random.seed(5)
    >>> r1 = {'a': 1, 'f': 1, 'g': 1, 'z': 1}
    >>> b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(r1, b, 7)
    >>> r1
    {'a': 1, 'f': 1, 'g': 1, 'z': 1, 's': 1, 'l': 1, 't': 1}
    >>> b
    {'a': 1, 'e': 2, 'h': 1, 'l': 1, 'n': 1, 'p': 2, 's': 2, 't': 1, 'z': 1}
    >>> r2 = {'b': 1}
    >>> refill_rack(r2, b, 8)
    >>> r2
    {'b': 1, 'n': 1, 'z': 1, 's': 2, 'a': 1, 't': 1, 'e': 1}
    >>> b
    {'e': 1, 'h': 1, 'l': 1, 'p': 2}
    >>> r3 = {'b': 1}
    >>> refill_rack(r3, b, 7)
    >>> r3
    {'b': 1, 'e': 1, 'l': 1, 'h': 1, 'p': 2}
    >>> b
    {}
    """
    # Representing the pool of letter as a list of letter
    list_of_pool_of_letters = dicts_utils.flatten_dict(pool_of_letters)
    amount_of_letter_to_draw = number_of_letters_desired_on_rack - len(dicts_utils.flatten_dict(rack)) # The amount of letter to draw
    
    amount_of_letter_drawned = 0 # Setting the amount of letter drawned from the rack at zero
    # Repeating the letter drawing as long as the amount of letter to draw is satisfied or there is no letter left on the rack
    while (amount_of_letter_drawned < amount_of_letter_to_draw) and (len(list_of_pool_of_letters) > 0):
        letter_drawn = random.choice(list_of_pool_of_letters) # Drawing a letter randomly from the list of letters in the pool
        if letter_drawn in rack:
            rack[letter_drawn] += 1 # Adding the letter drawned to the rack
        else:
            rack[letter_drawn] = 1 # Creating a new key: the letter drawned, and associate the value 1 (representing its count)
            
        pool_of_letters[letter_drawn] -= 1 # Removing the letter drawn from the pool of letters
        list_of_pool_of_letters.remove(letter_drawn) # Removing the letter drawn from list of letters in the pool
        amount_of_letter_drawned += 1
        # Removing the letter's key if this letter is no longer present in the pool
        if pool_of_letters[letter_drawn] == 0:
            pool_of_letters.pop(letter_drawn)
 
def compute_score(list_of_words, letter_point_dict, valid_words_dict):
    """
    (list, dict, dict) --> int
    Takes as input a list of strings representing the words inserted, a dictionary that
    maps each letters to the number of points that they are worth as well as a dictionary
    representing the entire set of valid words with the same format as that of the function
    dict_utils.create_scrabble_dict. The function returns the total score obtained from the words
    in the list of words. If a word in the list of words is not valid, then the total score is zero.
    
    >>> w = ['ant', 'apple', 'bar', 'barns', 'car', 'cabin']
    >>> p = {'a': 3, 's': 1, 't': 2, 'r': 4, 'i': -2, 'n': 3}
    >>> d = dicts_utils.create_scrabble_dict(w)
    >>> compute_score(['ant', 'bar'], p, d)
    15
    >>> compute_score(['orange', 'banana'], p, d)
    0
    >>> compute_score(['orange', 'car', 'cabin'], p, d)
    0
    >>> compute_score(['barns', 'ant', 'cash'], p, d)
    0
    """
    total_score = 0 # Setting the total score to zero
    # Iterate through each word of the list of word
    for word in list_of_words:
        if dicts_utils.is_valid_word(word, valid_words_dict):
            total_score += dicts_utils.get_word_score(word, letter_point_dict)
        else:
            total_score = 0
            return total_score # If the word is invalid, the total_score is set to zero and the loops end.
    return total_score
 
def place_tiles(board, letters_to_add, desired_row, desired_col, direction):
    """
    (list, str, int, int, str) --> list
    Takes as input a list of strings representing the board, a string representing the character to add
    on the board, two integers representing respectively the row and column numbers of the starting square
    as well as a string indicating the direction to place the letter ('right' or 'down'). The function
    adds the letters from letters_to_add in the direction specified (direction). The function returns
    the list of words that is generated from the letters that are added by the players.
    The order of the words on the list does not matter. If the direction input is not 'right' or 'down', an
    empty list is returned. Otherwise, the function returns the list of words that have been defined by letters
    that you have added.
    >>> b = board_utils.create_board(5, 6)
    >>> place_tiles(b, 'apple', 0, 0, 'right')
    ['apple']
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> place_tiles(b, 'ear', 1, 1, 'down')
    ['pear']
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], [' ', 'e', ' ', ' ', ' ', ' '], [' ', 'a', ' ', ' ', ' ', ' '], \
    [' ', 'r', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> place_tiles(b, 'lap', 1, 0, 'right')
    ['leap', 'al', 'pa', 'lp']
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], ['l', 'e', 'a', 'p', ' ', ' '], [' ', 'a', ' ', ' ', ' ', ' '], \
    [' ', 'r', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> place_tiles(b, 'lap', 1, 0, 'left')
    []
    """
    words_made_from_added_letters = [] # Creating an empty list of word made by the added letters
    if direction == 'right':
        # The letters_to_add will be added row-wise to the row with row number = desired_row
        list_where_letters_are_added = board[desired_row]
        # The position of the first added letter corresponds to the column with col_number = desired_col
        position_of_first_letter_to_be_added = desired_col    
    elif direction == 'down':
        # The letters_to_add will be added column-wise to the column with column number = desired_col
        list_where_letters_are_added = board_utils.get_vertical_axis(board, desired_col)
        # The position of the first added letter corresponds to the row with row_number = desired_row 
        position_of_first_letter_to_be_added = desired_row
    else:
        return words_made_from_added_letters
 
    # ADDING LETTERS TO THE BOARD
    index_of_letters_to_add = 0 # Setting the index of letters_to_add at zero
    list_of_position_of_added_letters = [] # Creating an empty list where the position of the added letters will be added
    
    # Iterate through index of element and the element of the list where letters will be added
    for element_index, element in enumerate(list_where_letters_are_added):
        # Making sure that the the first letter is added at the starting position,
        # that the letters are added at space character and that the index_of_letters_to_add do not go out of bond.
        if (element_index >= position_of_first_letter_to_be_added) and (element == ' ') and ((index_of_letters_to_add) < len(letters_to_add)):
            # Removing the space character from the list
            list_where_letters_are_added.pop(element_index)
            # Adding the corresponding letter of letters_to_add in place of the previously removed space character
            list_where_letters_are_added.insert(element_index, letters_to_add[index_of_letters_to_add])
            
            # When the direction is down, list_position_of_added_letters represents a deep copy of a board column, thus changing the list
            # doesn't change the column of the board. This must be done manually:
            if direction == 'down':
                # Adding the letter column-wise (thus index of added_letter = row_number of row where the letter was added)
                board[element_index][desired_col] = letters_to_add[index_of_letters_to_add]
                
            index_of_letters_to_add += 1 # Repeating the loop with the subsequent letter of letters_to_add
            # Noting the index of each added letter on the list(correspond to the col_number if direction is right or row_number if direction is down) 
            list_of_position_of_added_letters += [element_index]
    
    
    # MAIN WORD
    main_word_formed = board_utils.find_word(list_where_letters_are_added, position_of_first_letter_to_be_added)
    words_made_from_added_letters += [main_word_formed]
    
    
    # HOOK WORDS
    hook_word_formed = '' # An empty string representing the hook word formed
    for position_of_added_letter in list_of_position_of_added_letters:
        if direction == 'right': # If direction is right, hook words consist of column words formed by the added letters (so words are col-wise)
            list_containing_hook_word = board_utils.get_vertical_axis(board, position_of_added_letter)
            # The position of the first added_letters correspond to the desired row on the list_containing_one_added_letter
            position_of_first_letter_added = desired_row
        else: # If the direction is down, hook words consist of row words formed by the added letters (so words are row-wise)
            # Identifying the rows including one added letter (Down)
            list_containing_hook_word = board[position_of_added_letter]
            # The position of the first added_letters correspond to the desired col on the list_containing_one_added_letter
            position_of_first_letter_added = desired_col
        
        hook_word_formed = board_utils.find_word(list_containing_hook_word, position_of_first_letter_added)
        
        # Making sure that only word consisting of more than 1 character are added to the words_made_from_added_letters)
        if len(hook_word_formed) > 1:
            words_made_from_added_letters += [hook_word_formed]
    
    return words_made_from_added_letters
 
def make_a_move(board, rack, letters_to_add, desired_row, desired_col, direction):
    """
    (list, dict, int, int, str) --> list
    Takes as input a list of string representing the board, a dictionary representing the rack of the player,
    a string representing the letters the player wants to place, two integers representing, respectively, the row
    and column that the player wants to place the first letter that the player wants to place
    and a string indicating the direction that the letters are to be placed ('down', 'right'). If the
    direction is neither 'down' nor 'right', the functions terminates right away and returns an empty list
    Otherwise, the function checks if the move is valid; that is, if it follows the following requirements:
    1. Is there enough space on the board to place the letters
    2. Does the letters that the player places are present in his rack
    If condition 1 is not valid, the function raises an IndexError with appropriate message
    If condition 2 is not valid, the function raises a ValueError with appropriate message
    If an error is raised, the board and the rack remain unchanged
    If the 2 conditions are satisified, the move is executed and the rack and board changes accordingly
    
    >>> b = [['a', 'p', 'p', 'l', 'e', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    >>> r = {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 2}
    >>> make_a_move(b, r, 'cat', 0, 0, 'right')
    Traceback (most recent call last):
    ...
    IndexError: There is not enough space on the board
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> r == {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 2}
    True
    >>> make_a_move(b, r, 'bat', 3, 1, 'down')
    Traceback (most recent call last):
    ...
    IndexError: There is not enough space on the board
    >>> make_a_move(b, r, 'ack', 1, 1, 'down')
    Traceback (most recent call last):
    ...
    ValueError: Rack of player does not contain all the letters to be added
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> r == {'a': 1, 'b': 2, 'e': 1, 'k': 1, 's': 1, 't': 2}
    True
    >>> make_a_move(b, r, 'ast', 1, 1, 'down')
    ['past']
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], [' ', 'a', ' ', ' ', ' ', ' '], \
    [' ', 's', ' ', ' ', ' ', ' '], [' ', 't', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> r == {'b': 2, 'e': 1, 'k': 1, 't': 1}
    True
    >>> make_a_move(b, r, 'tb', 1, 0, 'right')
    ['tab', 'at', 'pb']
    >>> b == [['a', 'p', 'p', 'l', 'e', ' '], ['t', 'a', 'b', ' ', ' ', ' '], \
    [' ', 's', ' ', ' ', ' ', ' '], [' ', 't', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    True
    >>> r == {'b': 1, 'e': 1, 'k': 1}
    True
    
    """
    # Checking Available Space
    if direction == 'right':
        # The letters are added to a row of the board
        list_in_board_to_add_letters = board[desired_row]
        # The position of the row where the first letter is added (corresponds to a column of the board)
        position_of_starting_element = desired_col
    else:
        # The letters are added to a row of the board
        list_in_board_to_add_letters = board_utils.get_vertical_axis(board, desired_col)
        # The position of the row where the first letter is added (corresponds to a column of the board)
        position_of_starting_element = desired_row
    
    # Check if Enough Space (Condition 1)
    if not board_utils.fit_on_board(list_in_board_to_add_letters, letters_to_add, position_of_starting_element):
        raise IndexError('There is not enough space on the board')
    # Check if letters that the player wants to add are present in his rack (Condition 2)
    elif not has_letters(rack, letters_to_add):
        raise ValueError('Rack of player does not contain all the letters to be added')
    # If condition 1 and 2 are satisfied
    else:
        return place_tiles(board, letters_to_add, desired_row, desired_col, direction)