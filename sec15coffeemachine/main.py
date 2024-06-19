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

totalMoney = 0
moreCoffee = True
while(moreCoffee == True):
    uInput = input("What would you like? (espresso/latte/cappuccino):")
    #check resources
    if uInput == 'espresso':
        #checking for water and coffee
        if (resources['water'] >= MENU['espresso']['ingredients']['water']) and (resources['coffee'] >= MENU['espresso']['ingredients']['coffee']):
                #action
                print('please insert coins')
                nquarters = int(input('how many quarters? '))
                ndimes = int(input('how many dimes? '))
                nnickles = int(input('how many nickles? '))
                npennies = int(input('how many pennies? '))
                value = 0.25*nquarters+0.1*ndimes+0.05*nnickles+0.01*npennies
                
                #checking the inserted value
                if value >= MENU['espresso']['cost']:
                    change = value-MENU['espresso']['cost']
                    print(f"Here is ${change} in change.")

                    print('sure, workin on ur espresso')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                    resources['water'] -= MENU['espresso']['ingredients']['water']
                    totalMoney += MENU['espresso']['cost']
            
                    #printing resources left
                    print(f"remaining coffee: {resources['coffee']}, remaining water: {resources['water']}, remaining milk: {resources['milk']}")

                    coffeeIteration = input("do you want more coffee Y or N: ")
                    if coffeeIteration == 'Y':
                        moreCoffee = True
                    else:
                        morecoffee = False
                else:
                    moreCoffee = 'lessmoney'

        else:
            #shortage in resources
            if resources['water'] < MENU['espresso']['ingredients']['water']:
                 print('Sorry there is not enough water')
            elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                 print('Sorry there is not enough coffee')
            moreCoffee = 'empty'

    elif uInput == 'latte':
        #checking for water and coffee and milk
        if (resources['water'] >= MENU['latte']['ingredients']['water']) and (resources['coffee'] >= MENU['latte']['ingredients']['coffee']) and (resources['milk'] >= MENU['latte']['ingredients']['milk']):
                #action
                print('please insert coins')
                nquarters = int(input('how many quarters? '))
                ndimes = int(input('how many dimes? '))
                nnickles = int(input('how many nickles? '))
                npennies = int(input('how many pennies? '))
                value = 0.25*nquarters+0.1*ndimes+0.05*nnickles+0.01*npennies
                
                if value >= MENU['latte']['cost']:
                    change = value-MENU['latte']['cost']
                    print(f"Here is ${change} in change.")

                    print('sure, workin on ur latte')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                    resources['water'] -= MENU['latte']['ingredients']['water']
                    resources['milk'] -= MENU['latte']['ingredients']['milk']
                    totalMoney += MENU['latte']['cost']
            
                    #printing resources left
                    print(f"remaining coffee: {resources['coffee']}, remaining water: {resources['water']}, remaining milk: {resources['milk']}")
            
                    coffeeIteration = input("do you want more coffee Y or N: ")
                    if coffeeIteration == 'Y':
                        moreCoffee = True
                    else:
                        morecoffee = False
                else:
                    moreCoffee = 'lessmoney'
        else:
            #shortage in resources
            if resources['water'] < MENU['latte']['ingredients']['water']:
                 print('Sorry there is not enough water')
            elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                 print('Sorry there is not enough coffee')
            elif resources['milk'] < MENU['latte']['ingredients']['milk']:
                 print('Sorry there is not enough milk')
            moreCoffee = 'empty'

    elif uInput == 'cappuccino':
        #checking for water and coffee and milk
        if (resources['water'] >= MENU['cappuccino']['ingredients']['water']) and (resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']) and (resources['milk'] >= MENU['cappuccino']['ingredients']['milk']):
                #action
                print('please insert coins')
                nquarters = int(input('how many quarters? '))
                ndimes = int(input('how many dimes? '))
                nnickles = int(input('how many nickles? '))
                npennies = int(input('how many pennies? '))
                value = 0.25*nquarters+0.1*ndimes+0.05*nnickles+0.01*npennies
                
                if value >= MENU['cappuccino']['cost']:
                    change = value-MENU['cappuccino']['cost']
                    print(f"Here is ${change} in change.")
                
                    print('sure, workin on ur cappuccino')
                    print('here u go')

                    #updating resources
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                    resources['water'] -= MENU['cappuccino']['ingredients']['water']
                    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                    totalMoney += MENU['cappuccino']['cost']
            
                    #printing resources left
                    print(f"remaining coffee: {resources['coffee']}, remaining water: {resources['water']}, remaining milk: {resources['milk']}")
            
                    coffeeIteration = input("do you want more coffee Y or N: ")
                    if coffeeIteration == 'Y':
                        moreCoffee = True
                    else:
                        morecoffee = False
                else:
                    moreCoffee = 'lessmoney'
        else:
            #shortage in resources
            if resources['water'] < MENU['cappuccino']['ingredients']['water']:
                 print('Sorry there is not enough water')
            elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                 print('Sorry there is not enough coffee')
            elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
                 print('Sorry there is not enough milk')
            moreCoffee = 'empty'
    elif uInput == 'off':
         moreCoffee = 'off'
    elif uInput == 'report':
         print(f"""Coffee: {resources['coffee']} \nWater: {resources['water']} \nMilk: {resources['milk']}\nMoney: {totalMoney}""")


if moreCoffee == 'empty':
     print('shortage of resources, we are down for maintenance, thank you')
elif moreCoffee == 'off':
     print('coffee machine turned off for maintenance, thank you')
elif moreCoffee == 'lessmoney':
     print('Sorry that is not enough money. Money refunded')




                




