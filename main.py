from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of Menu, CoffeeMaker, and MoneyMachine
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order_asking = input(f"What would you like?: {coffee_menu.get_items()} ")  #get the order
    if order_asking == "off":  # if user chooses off then exits program
        is_on = False
    elif order_asking == "report":
        coffee_maker.report()  # corrected method call to use coffee_maker object
        money_machine.report()
    else:
        coffee_item = coffee_menu.find_drink(order_asking)  #get the menuitem selected by user
        if coffee_item is not None:  # Check if the drink exists in the menu
            cost_of_drink = coffee_item.cost   #get the cost of drink
            if coffee_maker.is_resource_sufficient(coffee_item): #if resources are sufficient then make coffee
                if money_machine.make_payment(cost_of_drink): #checks if money given is sufficient
                    coffee_maker.make_coffee(coffee_item) #if money is enough then make the coffee
                else:
                    is_on = False
            else:
                print("Sorry, there are not enough resources to make your drink.")
        else:
            print("Invalid selection. Please choose a valid drink or type 'off' to exit.")
