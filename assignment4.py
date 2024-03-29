# assignment4.py
 
# Question 1
def brick_tower(large_bricks, small_bricks, height):
    """
    (int, int, int) -> bool
    Takes as inputs the number of large bricks, the number of small bricks and the height
    of the tower to build. The size of the bricks are as follow: large brick = 7 inches
    small bricks  = 2 inches. The function returns True if you can build a brick tower of
    input heigh and False if you cannot. The inputs are assumed to be non-negative. A tower of
    height = 0 always return True.
    >>> brick_tower(4, 5, 0)
    True
    >>> brick_tower(5, 3, 41)
    True
    >>> brick_tower(3, 9, 50)
    False
    >>> brick_tower(3, 0, 15)
    False
    >>> brick_tower(1, 4, 15)
    True
    >>> brick_tower(0, 0, 0)
    True
    >>> brick_tower(0, 0, 1)
    False
    >>> brick_tower(4, 5, 34)
    True
    """
    if large_bricks*7 <= height:
        height -= 7*large_bricks
    else:
        height = (height % 7)
    return (height % 2 == 0) and (height <= 2*small_bricks)
 
    
# Question 2
 
def get_triangle(n, s):
    """
    (int, str) -> str
    Takes as an integer (n) that is non-negative and a string (s) representing a symbol.
    The function returns a string representing a triangle of height n with the symbol defined by s.
    If n is a negative number, a ValueError is raised with the message: the integer should be non-negative.
    Moreover, if s does not contain at least one character or if it contains only the space character,
    a ValueError is also raised with the message: the string should countain at least one character that is
    not a space character. The function checks the input validation first and then proceeds if the input are valid.
    >>> get_triangle(0, 'a')
    ''
    >>> get_triangle(0, ' ')
    Traceback (most recent call last):
    ...
    ValueError: the string should countain at least one character that is not a space character
    >>> c = get_triangle(1, ' ')
    Traceback (most recent call last):
    ...
    ValueError: the string should countain at least one character that is not a space character
    >>> c = get_triangle(-2, 'a')
    Traceback (most recent call last):
    ...
    ValueError: the integer should be non-negative
    >>> get_triangle(3, '') 
    Traceback (most recent call last):
    ...
    ValueError: the string should countain at least one character that is not a space character
    >>> c = get_triangle(3, ' a')
    >>> print(c)
     a 
     a  a 
     a  a  a 
     a  a 
     a 
    >>> c = get_triangle(2, '%')
    >>> print(c)
    % 
    % % 
    % 
    >>> c = get_triangle(5, 'banana')
    >>> print(c)
    banana 
    banana banana 
    banana banana banana 
    banana banana banana banana 
    banana banana banana banana banana 
    banana banana banana banana 
    banana banana banana 
    banana banana 
    banana 
    """
    if n < 0:
        raise ValueError('the integer should be non-negative')
    if (len(s) == 0) or s == ' ':
        raise ValueError('the string should countain at least one character that is not a space character')
    # Creating an empty list
    final_list = []
    for i in range(n-1, 0, -1):
        line = (s + ' ') * i
        # Adding the line on both sides of the list (corresponding to their 2 occurences on the triangle)
        final_list.append(line)
        final_list.reverse()
        final_list.append(line)
    # Adding the string corresponding to the height of the triangle (s * n) at the index corresponding to its only occurence
    height_line = (s + ' ') * n
    final_list.insert(n-1, height_line)
    return '\n'.join(final_list)
 
# Question 3
def sort_numbers(integer_list):
    """
    (list) --> NoneType
    Take as input a dimensional list of integer. The function re-arranges the elements of the list so that the
    even numbers (0 included) appear at the beginning of the list and the odd numbers appear at the end.
    The order of the numbers does not matter. The function does not return anything, but modifies the input list.
    >>> a = [2, 5, 6, 0, 1, 8, 10]
    >>> sort_numbers(a)
    >>> a
    [10, 0, 2, 6, 8, 1, 5]
    >>> a = []
    >>> sort_numbers(a)
    >>> a
    []
    >>> a = [0, 1, 2, -3, 4, 5, 5]
    >>> sort_numbers(a)
    >>> a
    [0, 2, 4, 5, -3, 1, 5]
    >>> a = [2, 4, 6, 8]
    >>> sort_numbers(a)
    >>> a
    [8, 6, 4, 2]
    """
    # Marking the index of even number as the uppermost left of the list
    even_index = 0
    # Marking the index of odd number as the uppermost right of the list
    odd_index = len(integer_list) - 1
    # Iterating through each number (and their index) of the list
    for i, num in enumerate(integer_list):
        # Removing the number from the list
        integer_list.pop(i)
        
        if (num % 2 == 0):
            integer_list.insert(even_index, num)
        else:
            integer_list.insert(odd_index, num)
            
# Question 4
def select_vector(x, y):
    """
    (list, list) --> list
    Takes as input a 2D-list of integer (x) as well as a list of indices. The
    function returns a 1D-list that contains the elements of the sublist of x
    at the position specified by y, the list of indices. The function raises a
    ValueError if y contains too few or too many elements or if the indices specified
    in y goes out of bound
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20], [0, 1, 4, 5]]
    >>> y = [-3, -2, -1, 2]
    >>> select_vector(x, y)
    [5, -4, 20, 4]
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20], [0, 1, 4, 5], [0]]
    >>> y = [0, -2, -1, 2]
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The list y contains too few or too many elements
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20], [0, 1, 4, 5], []]
    >>> y = [0, -2, -1, 2, 0]
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The indices of y are out of bound
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20], [0, 1, 4, 5], []]
    >>> y = [0, -2, -1, 2]
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The list y contains too few or too many elements
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20]]
    >>> y = [0, -2, -1, 2] 
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The list y contains too few or too many elements
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20]]
    >>> y = [0, -2, 5]
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The indices of y are out of bound
    >>> x = [[5, 6, 2], [1, -4, 2], [1, 4, 6, 3, 20]]
    >>> y = [-9, -6, -9]
    >>> select_vector(x, y)
    Traceback (most recent call last):
    ...
    ValueError: The indices of y are out of bound
    >>> x = [[8, 7, 6], [-5, 4], [3, 2, 1]]
    >>> y = [1, 1, 1]
    >>> select_vector(x, y)
    [7, 4, 2]
    >>> x = [[8, 7, 6], [-5, 4], [3, 2, 1]]
    >>> y = [2, -2, 2]
    >>> select_vector(x, y)
    [6, -5, 1]
    """
    # Creating a return_list
    return_list = []
    # Iterating through the sub-list and their index of x
    for index, x_sublist in enumerate(x):
        # Checking if the indice in y is in bound with the x_sublist (first part = positive index out of bound, second part = negative index out of bound)
        if ((len(x_sublist)-1) < y[index] or len(x_sublist) < abs(y[index])):
            raise ValueError("The indices of y are out of bound")
        if len(x) != len(y):
            raise ValueError("The list y contains too few or too many elements")
        
        return_list.append(x_sublist[y[index]])
    return return_list
 
# Question 5
def get_coordinates(w, target):
    """
    (list, str) --> list
    Takes as input a 2-dimensional list of string as well as a string called target.
    The function returns a list of tuples with the indices of where target appears in w
    The function is case sensitive.
    >>> w = [['2', 'a'], ['happy', '(1, 2)', '[]'], ['a', 'happy', 'HAPPY'], ['2', 'a', (1,2)], []]
    >>> get_coordinates(w, 'a')
    [(0, 1), (2, 0), (3, 1)]
    >>> get_coordinates(w, 'happy')
    [(1, 0), (2, 1)]
    >>> get_coordinates(w, 'HAPPY')
    [(2, 2)]
    >>> get_coordinates(w, '2')
    [(0, 0), (3, 0)]
    >>> get_coordinates(w, '(1, 2)')
    [(1, 1)]
    >>> get_coordinates(w, '1')
    []
    >>> get_coordinates(w, '[]')
    [(1, 2)]
    >>> get_coordinates(w, 'b')
    []
    >>> w = [['', ' '], ['happy', ' ', ''], ['a', 'happy', 'HAPPY'], ['b', 'a', '1'], []]
    >>> get_coordinates(w, 'b')
    [(3, 0)]
    >>> get_coordinates(w, '')
    [(0, 0), (1, 2)]
    >>> get_coordinates(w, ' ')
    [(0, 1), (1, 1)]
    """
    target_indices_list = []
    # Iterating through the index of sublist and sublist of w
    for index_sublist, sublist in enumerate(w):
        # Iterating through the index of element and the element of the sublist of w
        for index_element, element in enumerate(sublist):
            if element == target:
                target_indices_list += [(index_sublist, index_element)]
    
    return target_indices_list
 
# Question 6
def evaluate_polynomial(poly_dict, x):
    """
    (dict, float) --> float -or- int
    Takes as input a dictionary in which the key represents the powers of the polynomial and
    the value represents the coefficient of the polynomial. The key-value pair represents
    a power-coefficient pairs. Further, the function takes as input a value x representing the
    variable of the polynomial.
    
    >>> evaluate_polynomial({5: 6, 4: 0, 3: 1, 2: -4, -5: 20}, 2)
    184.625
    >>> evaluate_polynomial({-5: 6, 4: 0, 3: 1, 2: -4, -5: 20}, 2)
    -7.375
    >>> evaluate_polynomial({-5: 6, 4: 0, 3: 1, 2: -4, -5: 20}, -3)
    -63.08230452674897
    >>> evaluate_polynomial({2: 1, 0: 1}, -9)
    82
    >>> evaluate_polynomial({2.5: 3.1, 0.6: 7.7, 0: 8.87}, 9.85)
    983.2046579663324
    >>> evaluate_polynomial({2.5: 3.1, 0.6: 7.7, 0: 8.87}, 1.5)
    27.233364132774916
    """
    poly_value = 0
    for k, v in poly_dict.items():
        poly_value += v * x**k
    return poly_value
 
# Question 7
def anagrams(list_of_words, specified_word):
    """
    (list, str) --> bool
    Take as input a list of words as well as a specified word and check
    if the words in the list of words are anagrams of the specified word.
    If all the words on the list are anagrams of the specified word, the function
    returns True. If one of the word is not an anagram of the specified word, the
    function returns False.
    >>> anagrams(['arts', 'rats', 'tsar'], 'star')
    True
    >>> anagrams(['ACER', 'AcRe', 'cARE'], 'care')
    True
    >>> anagrams(['ace', 'AcRe', 'cARE', 'race'], 'care')
    False
    >>> anagrams(['ace', 'AcRe', 'cARE'], 'car')
    False
    >>> anagrams(['moon starer'], 'astronomer')
    False
    >>> anagrams(['shear', 'RHEAS', 'HARES', 'share', 'SHARE'], 'SHARE')
    True
    """
    # Creating a list of dictionaries (that will represent the occurence of characters)
    list_of_dict = []
    # Adding the specified word to the list_of_words
    list_of_words += [specified_word]
    # Iterating through the words of the list_of_words
    for word in list_of_words:
        # Creating a new dictionary representing the character count of each word
        char_count_dict = dict()
        # Iterating through the character of the word
        for char in word.lower():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
        # Adding the dictionary to the list
        list_of_dict += [char_count_dict]
        
    specified_word_dict = list_of_dict[-1]
    # Iterating through the dictionary on the list_of_dict and check if they contain the same key-value pairs
    for char_dict in list_of_dict:
        if specified_word_dict != char_dict:
            return False
    return True
   
# Question 8
import random
# HELPER-FUNCTION
def flatten_dict(input_dict):
    """
    (dict) --> list
    Takes as input a dictionary with string as key and non-negative integer as
    value and return a list containing the key's string appearing as many time as the value
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
# RE-DO THE DOCTEST ELEMENT
def refill_rack(rack, pool_of_letters, number_of_letters_desired_on_rack):
    """
    (dict, dict, int) --> NoneType
    Takes as input a dictionary representing the rack of the player, another dictionary
    representing the pool of letters and a positive integer representing the number of letter
    to be added onto the rack (provided that the pool has at least n letter). If the pool has less
    than n letters, than all the letters of the pool are picked. The function does not return any value,
    but modify the dictionaries representing the rack and pool of letter accordingly.
    >>> random.seed(10)
    >>> rack1 = {'a': 2, 's': 1, 'g': 1}
    >>> b = {'a': 2, 'b': 1, 'e': 3, 'm': 1, 'n': 1, 'p': 2, 'r': 4, 't': 1, 'x': 2, 'y': 1}
    >>> refill_rack(rack1, b, 9)
    >>> rack1
    {'a': 4, 's': 1, 'g': 1, 't': 1, 'y': 1, 'r': 1}
    >>> b
    {'b': 1, 'e': 3, 'm': 1, 'n': 1, 'p': 2, 'r': 3, 'x': 2}
    >>> refill_rack(rack1, b, 8)
    >>> rack1
    {'a': 4, 's': 1, 'g': 1, 't': 1, 'y': 1, 'r': 1}
    >>> b
    {'b': 1, 'e': 3, 'm': 1, 'n': 1, 'p': 2, 'r': 3, 'x': 2}
    >>> rack2 = {'e': 1, 'n': 1, 'z': 1}
    >>> refill_rack(rack2, b, 8)
    >>> rack2
    {'e': 3, 'n': 2, 'z': 1, 'r': 2}
    >>> b
    {'b': 1, 'e': 1, 'm': 1, 'p': 2, 'r': 1, 'x': 2}
    >>> rack3 = {'a':1}
    >>> refill_rack(rack3, b, 7)
    >>> rack3
    {'a': 1, 'b': 1, 'r': 1, 'p': 2, 'e': 1, 'm': 1}
    >>> b
    {'x': 2}
    >>> refill_rack(rack3, b, 9)
    >>> rack3
    {'a': 1, 'b': 1, 'r': 1, 'p': 2, 'e': 1, 'm': 1, 'x': 2}
    >>> b
    {}
    """
    # Representing the pool of letter as a list of letter
    list_of_pool_of_letters = flatten_dict(pool_of_letters)
    amount_of_letter_to_draw = number_of_letters_desired_on_rack - len(flatten_dict(rack)) # The amount of letter to draw
    
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
 
# Question 10
# Random was re-imported as it is a different question. I know that random was already import, but I re-imported to show that we must import random for this question!
import random
class Cake:
    """
    Represent a cake
    Instance Attributes: name (str), ingreds (list), price (float)
    """
    
    def __init__(self, name, ingreds):
        self.name = name
        if len(ingreds) < 3:
            raise ValueError("A cake must contain at least three ingredients")
        self.ingreds = ingreds
        self.price = random.randint(10, 14) + random.random()
        
    def __str__(self):
        """
        (Cake) --> str
        Take as input an object of type Cake and returns a string with the
        name of the cake and its price rounded to 2 decimals. This function
        does not change the values stored of the input object's instance attributes
        >>> random.seed(5)
        >>> a = Cake('Chocolate', ['Chocolate Cream', 'Milk', 'Eggs'])
        >>> a.__str__()
        'Chocolate Cake  $14.26'
        >>> a.ingreds == ['Chocolate Cream', 'Milk', 'Eggs']
        True
        >>> round(a.price, 2) == 14.26
        True
        >>> a.name == 'Chocolate'
        True
        >>> b = Cake('Vanilla', ['Vanilla Cream', 'White Chocolate', 'Eggs'])
        >>> str(b)
        'Vanilla Cake  $12.8'
        >>> b.name == 'Vanilla'
        True
        >>> b.ingreds == ['Vanilla Cream', 'White Chocolate', 'Milk']
        False
        >>> round(b.price, 2) == 12.8
        True
        >>> c = Cake('Bad Cake', ['Chocolate', 'Vanilla', 'Caramel'])
        >>> print(c)
        Bad Cake Cake  $14.03
        >>> c.name == 'Bad Cake Cake'
        False
        >>> c.ingreds == ['Chocolate', 'Vanilla', 'Caramel']
        True
        >>> round(c.price, 2) == 10.01
        False
        >>> d = Cake('Cheese', ['Cheese Cream', 'Graham Crackers'])
        Traceback (most recent call last):
        ...
        ValueError: A cake must contain at least three ingredients
        """
        return self.name + ' Cake ' + ' $' + str(round(self.price, 2))
    
    def is_better(self, other_cake):
        """
        (Cake, Cake) --> bool
        Takes as input an object of type cake as well as another object of type cake.
        The function calculates the ratio of the price vs the number of ingredients and
        return True if the first object of Type Cake has a lower ratio than the second inputed
        Cake and return False if the second (object) Cake has a lower ratio than the first one.
        If the ratio of price/num_of_ingredients are equal, the function returns False.
        >>> a = Cake('Chocolate', ['Chocolate Cream', 'Milk', 'Eggs', 'Banana', 'Chocolate Chip', 'Ice Cream'])
        >>> a.price = 13.50
        >>> b = Cake('Vanilla', ['Vanilla Cream', 'White Chocolate', 'Eggs', 'Orange'])
        >>> b.price = 10.21
        >>> a.is_better(b)
        True
        >>> c = Cake('Cheese', ['Cheese Cream', 'Chocolate Syrup', 'Graham Crackers', 'Sour Cream', 'Lemon'])
        >>> c.price = 11.25
        >>> c.is_better(a)
        False
        >>> c.price = 11.24
        >>> c.is_better(a)
        True
        >>> d = Cake('Bad Cake', ['Chocolate', 'Vanilla', 'Caramel'])
        >>> d.price = 14.95
        >>> b.is_better(d)
        True
        >>> d = Cake('Surprise', ['Chocolate', 'Vanilla'])
        Traceback (most recent call last):
        ...
        ValueError: A cake must contain at least three ingredients
        """
        ratio_self_cake = self.price/len(self.ingreds)
        ratio_other_cake = other_cake.price/len(other_cake.ingreds)
        return ratio_self_cake < ratio_other_cake
 
 
def create_menu(cake_name_to_ingreds):
    """
    (dict) --> list
    Takes as input a dictionary mapping the name of the cake (str) to their list of ingredients.
    From the dictionary, the function create and returns a list of Cake object with the name and ingredients
    specified by the key-value of the inputed dictionary. Further, the function display the menu one per line
    >>> random.seed(5)
    >>> a = {'Cheese': ['Cheese Cream', 'Chocolate Syrup', 'Graham Crackers'], 'Chocolate': ['Chocolate Cream', 'Milk', 'Eggs'], \
    'Vanilla': ['Vanilla Cream', 'White Chocolate', 'Orange'], 'Surprise': ['Chocolate', 'Vanilla', 'Caramel']}
    >>> menu = create_menu(a)
    Cheese Cake  $14.26
    Chocolate Cake  $12.8
    Vanilla Cake  $14.03
    Surprise Cake  $13.78
    >>> type(menu[0])
    <class '__main__.Cake'>
    >>> menu[0].name == 'Cheese'
    True
    >>> menu[0].ingreds == ['Cheese Cream', 'Chocolate Syrup', 'Graham Crackers']
    True
    >>> type(menu[1])
    <class '__main__.Cake'>
    >>> menu[1].name == 'Chocolate'
    True
    >>> menu[1].ingreds == ['chocolate Cream', 'milk', 'eggs']
    False
    >>> d =  {'Fruit': ['Banana', 'Apple'], 'Red Velvet': ['Cream Cheese', 'Vanilla icing', 'Food Colouring']}
    >>> menu = create_menu(d)
    Traceback (most recent call last):
    ...
    ValueError: A cake must contain at least three ingredients
    >>> d = {'Fruit': ['Banana', 'Apple', 123], 'Red Velvet': ['Cream Cheese', 'Vanilla icing', 'Food Colouring']}
    >>> menu = create_menu(d)
    Fruit Cake  $11.65
    Red Velvet Cake  $11.11
    >>> type(menu[0])
    <class '__main__.Cake'>
    >>> menu[0].name == 'fruit'
    False
    >>> menu[0].ingreds == ['Banana', 'Apple', 123]
    True
    """
    # Changing the dictionary into a list of tuples
    list_cake_name_to_ingreds = list(cake_name_to_ingreds.items())
    # Creating an empty list
    list_of_cakes = []
    # Iterating through the elements of the tuples
    for name, ingreds in list_cake_name_to_ingreds:
        new_object = Cake(name, ingreds)
        print(new_object)
        list_of_cakes.append(new_object)
    return list_of_cakes
 
def find_best(list_of_cakes):
    """
    (list) --> Cake
    Take as input a non-empty list of cake and returns the best cake from the list.
    If there is a tie between two cakes, the function returns the cake that appears
    first on the list.
    >>> random.seed(5)
    >>> a = {'Cheese': ['Cheese Cream', 'Chocolate Syrup', 'Graham Crackers'], 'Chocolate': ['Chocolate Cream', 'Milk', 'Eggs'], \
    'Vanilla': ['Vanilla Cream', 'White Chocolate', 'Orange'], 'Surprise': ['Chocolate', 'Vanilla', 'Caramel']}
    >>> cake_list = create_menu(a)
    Cheese Cake  $14.26
    Chocolate Cake  $12.8
    Vanilla Cake  $14.03
    Surprise Cake  $13.78
    >>> best = find_best(cake_list)
    >>> print(best)
    Chocolate Cake  $12.8
    >>> d = {'Fruit': ['Banana', 'Apple', 123], 'Red Velvet': ['Cream Cheese', 'Vanilla icing', 'Food Colouring']}
    >>> cake_list = create_menu(d)
    Fruit Cake  $11.65
    Red Velvet Cake  $11.11
    >>> best = find_best(cake_list)
    >>> print(best)
    Red Velvet Cake  $11.11
    >>> a = Cake('Chocolate', ['Chocolate Cream', 'Milk', 'Eggs', 'Banana', 'Chocolate Chip', 'Ice Cream'])
    >>> a.price = 13.50
    >>> b = Cake('Vanilla', ['Vanilla Cream', 'White Chocolate', 'Eggs', 'Orange'])
    >>> b.price = 10.21
    >>> c = Cake('Cheese', ['Cheese Cream', 'Chocolate Syrup', 'Graham Crackers', 'Sour Cream', 'Lemon'])
    >>> c.price = 11.25
    >>> d = Cake('Bad Cake', ['Chocolate', 'Vanilla', 'Caramel'])
    >>> d.price = 14.95
    >>> s = find_best([a, b, c, d])
    >>> s.name == 'Chocolate'
    True
    >>> s = find_best([c, a, b, d])
    >>> s.name == 'Cheese'
    True
    >>> s = find_best([d, b])
    >>> s.name == 'Vanilla'
    True
    >>> find_best([c, a, b, d, Cake('Fruit', ['Banana', 'Apple'])])
    Traceback (most recent call last):
    ...
    ValueError: A cake must contain at least three ingredients
    """
    # Setting the best cake to the first cake of the list_of_cakes
    best_cake = list_of_cakes[0]
    for cake in list_of_cakes:
        if cake.is_better(best_cake):
            best_cake = cake
    return best_cake