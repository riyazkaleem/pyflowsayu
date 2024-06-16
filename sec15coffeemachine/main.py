#coffee machine

#implementation
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffeeFunction():
    moreCoffee = True
    while(moreCoffee):
        uInput = input("What would you like? (espresso/latte/cappuccino):")

        #check resources
        if uInput == 'espresso':
            #checking for water and coffee
            if (resources['water'] >= MENU['espresso']['ingredients']['water']) and (resources['coffee'] >= MENU['espresso']['ingredients']['coffee']):
                    #action
                    print('sure, workin on ur espresso')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                    resources['water'] -= MENU['espresso']['ingredients']['water']
            else:
                #shortage in resources
                moreCoffee = False
                status = 'off'

        elif uInput == 'latte':
            #checking for water and coffee and milk
            if (resources['water'] >= MENU['latte']['ingredients']['water']) and (resources['coffee'] >= MENU['latte']['ingredients']['coffee']) and (resources['milk'] >= MENU['latte']['ingredients']['milk']):
                    #action
                    print('sure, workin on ur espresso')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                    resources['water'] -= MENU['latte']['ingredients']['water']
                    resources['milk'] -= MENU['latte']['ingredients']['milk']
            else:
                #shortage in resources
                moreCoffee = False
                status = 'off'

        elif uInput == 'cappuccino':
            #checking for water and coffee and milk
            if (resources['water'] >= MENU['cappuccino']['ingredients']['water']) and (resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']) and (resources['milk'] >= MENU['cappuccino']['ingredients']['milk']):
                    #action
                    print('sure, workin on ur espresso')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                    resources['water'] -= MENU['cappuccino']['ingredients']['water']
                    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            else:
                #shortage in resources
                moreCoffee = False
                status = 'off'
    return status, moreCoffee

#checking coffeemachine for status
coffeeStatus, moreCoffeeStatus = coffeeFunction()
if coffeeStatus == 'off':
     print('sorry, coffee machine is down for maintenance')

if moreCoffeeStatus == False:
     print('waiting for some time, cus dont want coffee')

#work for next time
#print report after every execution
#follow the coffee machine program requirements




                




