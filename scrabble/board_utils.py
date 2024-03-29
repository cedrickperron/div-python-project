# board_utils.py
 
def create_board(number_of_row, number_of_col):
    """
    (int, int) --> list
    Take as input two integer representing the number of rows and columns and
    return a 2-dimensional list of strings containing only space-character
    elements, which represent an empty square on the board. If the input integers
    are not both positive, a ValueError is raised with the message: the inputs must both be positive
    >>> create_board(2, 1)
    [[' '], [' ']]
    >>> create_board(3, 2)
    [[' ', ' '], [' ', ' '], [' ', ' ']]
    >>> create_board(0, 1)
    Traceback (most recent call last):
    ...
    ValueError: the inputs must both be positive
    >>> create_board(3, -5)
    Traceback (most recent call last):
    ...
    ValueError: the inputs must both be positive
    """
    # Create an empty board
    board = []
    
    if number_of_row <= 0 or number_of_col <= 0:
        raise ValueError('the inputs must both be positive')
    
    # Iterate through each row of the board through their row number
    for row_number in range(number_of_row):
        row = [] # Create an empty row
        # Iterate through each column of the board through their column number
        for col_number in range(number_of_col):
            # Add each column to the row
            row += ' '
        # Add each row to the board
        board.append(row)
    return board
 
def display_board(board):
    """
    (list) --> NoneType
    Take as input a two dimensional list of string representing the board
    and display the board, one row per line, and each row and column are identified
    by their corresponding number
    >>> b = create_board(2, 4)
    >>> display_board(b)
        0   1   2   3
      +---------------+
    0 |   |   |   |   | 
      +---------------+
    1 |   |   |   |   | 
      +---------------+
    >>> b = [['a', 'p', 'p', 'l', 'e', 's', ' ', ' '], ['n', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['t', 'a', 'k', 'e', 'a', 'w', 'a', 'y']]
    >>> display_board(b)
        0   1   2   3   4   5   6   7
      +-------------------------------+
    0 | a | p | p | l | e | s |   |   | 
      +-------------------------------+
    1 | n |   |   |   |   |   |   |   | 
      +-------------------------------+
    2 | t | a | k | e | a | w | a | y | 
      +-------------------------------+
    >>> b = [['o', 'r', 'a', 'n', 'g', 'e', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['t', 'a', 'k', 'e', 'a', 'w', 'a', 'y']]
    >>> display_board(b)
        0   1   2   3   4   5   6   7
      +-------------------------------+
    0 | o | r | a | n | g | e |   |   | 
      +-------------------------------+
    1 |   |   |   |   |   |   |   |   | 
      +-------------------------------+
    2 | t | a | k | e | a | w | a | y | 
      +-------------------------------+
    """
    number_of_row, number_of_col = len(board), len(board[0])
    
    # UPMOST LEFT (BEGIN)
    row_with_col_numbers = (4*' ') # Upmost Left of the row where columns are written
    board_contour = (2*' ' + '+-') # Upmost Left contour of the board
    # MIDDLE
    for col_number in range(number_of_col-1):
        if col_number <= 9:
            row_with_col_numbers += (str(col_number)+ 3*' ') # Add all the single digit col_number and separate them by 3 spaces from other col_number
        else:
            row_with_col_numbers += (str(col_number)+ 2*' ') # Add all the double digit col_number and separate them by 2 spaces from other col_number
        board_contour += (4*'-')# The contour of the board in between two columns is separated by 4 *'-'
    # UPMOST RIGHT (END)
    row_with_col_numbers += str(col_number+1) # Last col_number is added
    board_contour += '--+' # Upmost right of board contour
    # ROW LINE
    playing_rows_of_board = [] # Empty list of all the rows where the game is played
    # Iterating through each playable row of the board through their row number
    for row_number in range(number_of_row):
        if row_number <= 9:
            playing_board_row = (str(row_number) + ' | ') # Add single digit row number and left contour of board playable row
        else:
            playing_board_row = (str(row_number) + '| ') # If the row number is double digit remove a space from the left contour of the board
        for element_on_board in board[row_number]:
            playing_board_row += (element_on_board + ' | ') # Adding the board element to respective row and column on board and separating each column
        
        playing_rows_of_board.append(playing_board_row)
    # Displaying the board
    print(row_with_col_numbers) # First Line
    print(board_contour) # Upper Contour of the Board
    for playing_row in playing_rows_of_board:
        print(playing_row)
        print(board_contour)
 
def get_vertical_axis(board, col_number):
    """
    (list) --> list
    Takes as input a two dimensional list of strings representing the board as well as
    an integer representing the column number. It returns all the elements of  list on
    that columns as a list where all elements are represented as a string. The function
    assumes that the column number input exists in the board.
    
    >>> b = [['a', 'p', 'p', 'l', 'e', 's', ' ', ' '], ['n', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['t', 'a', 'k', 'e', 'a', 'w', 'a', 'y']]
    >>> get_vertical_axis(b, 0)
    ['a', 'n', 't']
    >>> b = [['o', 'r', 'a', 'n', 'g', 'e', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['t', 'a', 'k', 'e', 'a', 'w', 'a', 'y']]
    >>> get_vertical_axis(b, 1)
    ['r', ' ', 'a']
    >>> b = [['o', 'r', 'a', 'n', 'g', 'e', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['t', 'a', 'k', 'e', 'a', 'w', 'a', 'y']]
    >>> get_vertical_axis(b, 7)
    [' ', ' ', 'y']
    >>> b = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> get_vertical_axis(b, 2)
    ['t', 'r', 'a', 'i', 'n']
    """
    column = []
    for row in board:
        column.append(row[col_number])
    return column
        
def find_word(list_with_elements, position_of_starting_element_of_word):
    """
    (list, int) --> str
    Takes as input a list of string and an integer and returns the string
    built by concatenating the sequence of consecutive string starting at the position i that are not space character.
    If the string at position i corresponds to a space character, the function returns an empty string.
    
    >>> find_word(['a', 'p', 'p', 'l', 'e', 's', ' ', ' '], 0)
    'apples'
    >>> find_word(['a', 'p', 'p', 'l', 'e', 's', ' ', ' '], 1)
    'apples'
    >>> find_word(['appl', 'e', 's', ' '], 0)
    'apples'
    >>> find_word(['ban', ' ', 'ana', ' '], 0)
    'ban'
    >>> find_word(['ban', '', 'ana', ' '], 1)
    'banana'
    >>> find_word(['ban', ' ', 'ana', ' '], 1)
    'ban'
    >>> find_word([' ', 'squi', '', 'rre', 'l'], 2)
    'squirrel'
    """
    desired_word = ''    # The desired word
    if list_with_elements[position_of_starting_element_of_word] == ' ':
        return desired_word # if the starting element is a space, then an empty string is returned
    
    index = position_of_starting_element_of_word #Setting the index to the position_of_starting_element_of_word
    # Interating backward through the index until the character associated to one of the index is a space character or the index reach -1
    while (index != -1) and (list_with_elements[index] != ' '):
        index -= 1
    # The position of the first element of the word
    index_of_starting_element_of_word = index + 1
    
    # Iterating through the element of word until you reach a space character
    for index_of_word in range(index_of_starting_element_of_word, len(list_with_elements)):
        if list_with_elements[index_of_word] == ' ':
            break
        desired_word += list_with_elements[index_of_word]
    return desired_word
 
def available_space(list_of_board, position_of_starting_element):
    """
    (list, int) --> int
    Takes as input a list of string corresponding to a row or a column of the board as
    well as an integer i and returns the number of empty squares on the row/colum starting
    from the position defined by i.
    >>> available_space(['ban', '', 'ana', ' '], 1)
    1
    >>> available_space(['a', 'p', 'p', 'l', 'e', 's', ' ', ' '], 0)
    2
    >>> r = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> available_space(r, 2)
    5
    >>> c = ['a', 'n', 't']
    >>> available_space(c, 0)
    0
    """
    # Removing all elements of the list of string occuring before the starting element
    adjusted_list_of_board = list_of_board[position_of_starting_element:]
    # Counting the number of available space or (space character)
    number_of_space = adjusted_list_of_board.count(' ')
    return number_of_space
 
def fit_on_board(list_of_board, letters, position_of_starting_element):
    """
    (list, int) --> bool
    Takes as input a list of string representing a playable row/column of the
    board, a string called letters representing the desired word to be inserted and
    an integer i representing the position at which the first letter of letters is to be inserted.
    It returns a boolean value indicating if there is enough space for the letter to fit. Each square
    can contain only one character. The function should not modify the input list
    >>> r = ['r', 'r', 't', ' ', ' ', ' ', ' ', 'r']
    >>> fit_on_board(r, 'cat', 3)
    True
    >>> r
    ['r', 'r', 't', ' ', ' ', ' ', ' ', 'r']
    >>> r = [' ', 'r', ' ', 't', ' ', ' ', ' ', 'r']
    >>> fit_on_board(r, 'cat', 2)
    True
    >>> r
    [' ', 'r', ' ', 't', ' ', ' ', ' ', 'r']
    >>> r = [' ', 'r', 't', 'd', ' ', '', ' ', 'r']
    >>> fit_on_board(r, 'dog', 4)
    False
    >>> r
    [' ', 'r', 't', 'd', ' ', '', ' ', 'r']
    >>> r = [' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 't']
    >>> fit_on_board(r, 'apple', 2)
    True
    >>> r
    [' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 't']
    """
    # Counting the space taken by the input word
    space_required_for_letters_to_fit = len(letters)
    
    return space_required_for_letters_to_fit <= available_space(list_of_board, position_of_starting_element)
 