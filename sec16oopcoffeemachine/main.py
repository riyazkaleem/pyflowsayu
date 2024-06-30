from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#creating objects
mymoneymachine = MoneyMachine()
mycoffeemaker = CoffeeMaker()
mymenu = Menu()

#implementation
is_on = True
while is_on:
    currentmenu = mymenu.get_items()
    userinp = input(f'what do you wanna have from the menu: {currentmenu}? ')
    print('somethin')
    if userinp == 'off':
        print('bye bye for the maintanance')
        is_on = False
    
    elif userinp == 'report':
        mycoffeemaker.report()
        mymoneymachine.report()

    else:
        curdrink = mymenu.find_drink(userinp)
        print(curdrink)