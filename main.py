from data import resources
from data import MENU


def check_resources(customer):
    if resources['water'] >= MENU[customer]['ingredients']['water']:
        if resources['coffee'] >= MENU[customer]['ingredients']['coffee']:
            if 'milk' in MENU[customer]['ingredients']:
                if resources['milk'] >= MENU[customer]['ingredients']['milk']:
                    return 'good'
                else:
                    return 'Sorry there is not enough milk.'
            else:
                return 'good'
        else:
            return 'Sorry there is not enough coffee.'
    else:
        return 'Sorry there is not enough water.'


def coffee_machine():
    customer = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if customer == 'off':
        print('Coffee machine has turned off.')
    elif customer == 'report':
        print('Water: ', resources['water'], 'ml')
        print('Milk: ', resources['milk'], 'ml')
        print('Coffee: ', resources['coffee'], 'g')
        print('Money: ', resources['money'], '$')
        coffee_machine()
    else:
        if check_resources(customer) == 'good':
            print('Please insert coins.')
            quarter = round(float(input('How many quarters?: ')) * 0.25, 2)
            dimes = round(float(input('How many dimes?: ')) * 0.1, 2)
            nickles = round(float(input('How many nickles?: ')) * 0.05, 2)
            pennies = round(float(input('How many pennies?: ')) * 0.01, 2)
            money = quarter + dimes + nickles + pennies

            if money >= MENU[customer]['cost']:
                change = money - MENU[customer]['cost']
                if change > 0.00:
                    print(f'Here is ${round(change, 2)} dollars in change.')
                resources['money'] += MENU[customer]['cost']
                resources['water'] -= MENU[customer]['ingredients']['water']
                resources['coffee'] -= MENU[customer]['ingredients']['coffee']
                if customer != 'espresso':
                    resources['milk'] -= MENU[customer]['ingredients']['milk']
                print(f'Here is your {customer} ☕. Enjoy!')
            else:
                print('You didnt put enough money.')
                print('Your money is refunded.')
        else:
            print(check_resources(customer))
        coffee_machine()


coffee_machine()
