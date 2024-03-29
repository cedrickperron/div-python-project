# ADDED IMPORT
import math as m
 
def display_welcome_menu():
    print("Welcome to COMP 202 fair pizza calculator!")
    print("Please choose one of the following modes:")
    print("A. \"Quantity mode\"\nB. \"Price mode\"")
# ADDED FUNCTION
def ratio_of_pizzas(diameter_of_large_pizza,diameter_of_small_pizza):
    """
    This function takes two numbers input:
    1) diameter of the large pizza
    2) diameter of small pizza
    The function calculates the ratio of diameters of the large pizza (1st input) divided by the diameter of the small pizza (2nd input)
    The function puts the ratio of the diameter as global variable (so that its values is kept throughout the program)
    The function calculates the ratio of the areas of the pizzas from the ratio of their diameters
    The function puts the variable representing the ratio of the areas of the pizzas as global variable (so that its values is kept throughout the program)
    The function guarantees that the ratio of the areas of the pizzas is calculated as the area of the largest pizza divided by the area of the smallest pizza.
    >>> ratio_of_pizzas(10,2)
    25.0
    >>> ratio_of_pizzas(2,10)
    25.0
    >>> ratio_of_pizzas(6,2)
    9.0
    >>> ratio_of_pizzas(6.5,2.2)
    8.729338842975205
    """
    global ratio_of_diameters
    ratio_of_diameters = diameter_of_large_pizza/diameter_of_small_pizza
    global ratio_of_areas_of_pizzas
    ratio_of_areas_of_pizzas = m.pow(ratio_of_diameters,2)
    if ratio_of_areas_of_pizzas >=1:
        return ratio_of_areas_of_pizzas
    else:
        ratio_of_areas_of_pizzas = m.pow(ratio_of_areas_of_pizzas, -1)
        return ratio_of_areas_of_pizzas
 
def get_fair_quantity(diameter_of_large_pizza,diameter_of_small_pizza): 
    ratio_of_pizzas(diameter_of_large_pizza,diameter_of_small_pizza) 
    global min_number_of_small_pizza_for_equi 
    min_number_of_small_pizza_for_equi = m.ceil(ratio_of_areas_of_pizzas) 
    return min_number_of_small_pizza_for_equi 
    
def get_fair_price(diameter_of_large_pizza, price_of_large_pizza, diameter_of_small_pizza, amout_of_small_to_buy): 
    ratio_of_pizzas(diameter_of_large_pizza,diameter_of_small_pizza) 
    global price_to_pay_for_small_pizza 
    price_to_pay_for_small_pizza = round((amout_of_small_to_buy*price_of_large_pizza*m.pow(ratio_of_areas_of_pizzas, -1)), 2)  
    return price_to_pay_for_small_pizza 
  
def run_pizza_calculator(): 
    display_welcome_menu() 
    choice_of_mode = input("Enter your choice: ")
    if choice_of_mode == "A":
        print("You selected \"Quantity mode\" \n")
        diameter_of_large_pizza = int(input("Enter the diameter of the large pizza: "))
        diameter_of_small_pizza = int(input("Enter the diameter of the small pizza: "))
        get_fair_quantity(diameter_of_large_pizza,diameter_of_small_pizza)
        print("\nTo be fully satisfied, you should order", min_number_of_small_pizza_for_equi, "small pizzas")
    elif choice_of_mode == "B":
        print("You selected \"Price mode\" \n")
        diameter_of_large_pizza = int(input("Enter the diameter of the large pizza: "))
        price_of_large_pizza = float(input("Enter the price of the large pizza: "))
        diameter_of_small_pizza = int(input("Enter the diameter of the small pizza: "))
        amout_of_small_to_buy = int(input("Enter the number of small pizzas you'd like to buy: "))
        get_fair_price(diameter_of_large_pizza, price_of_large_pizza, diameter_of_small_pizza, amout_of_small_to_buy)
        print("\nThe fair price to pay for", amout_of_small_to_buy, "small pizzas is $"+ str(price_to_pay_for_small_pizza))
    else:
        print("\nThis mode is not supported")