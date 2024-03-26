from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice_text = """What would you like to do?
    > Order espresso: type "espresso"
    > Order latte: type "latte"
    > Order cappuccino: type "cappuccino"
    > See machine stock: type "report"
    > Set machine off: type "off"
    """
    choice = input(choice_text)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
