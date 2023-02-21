from menu import MENU, resources


def till(choice):
    print(f"Please insert {choice['cost']}")
    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickles = float(input('How many nickles?: '))
    pennies = float(input('How many pennies?: '))

    total = quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01

    change = total - choice['cost']
    profit = choice['cost']

    return change, profit


def process_payment(change):
    if change > 0 or change == 0:
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {user_order} ☕. Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")


def update_resources(choice, resources):
    if user_order == 'espresso':
        resources['water'] -= choice['ingredients']['water']
        resources['coffee'] -= choice['ingredients']['coffee']
        return resources
    else:
        resources['water'] -= choice['ingredients']['water']
        resources['milk'] -= choice['ingredients']['milk']
        resources['coffee'] -= choice['ingredients']['coffee']
        return resources


def check_resources(resources, ingredients):
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there's not enough {i}")
            return False
    return True


# TODO 1. Prompt user by asking "What you would like? (expresso/latte/cappuccino):

off = False
profit = 0
while not off:

    user_order = input('What would you like? (expresso/latte/cappuccino) ')

    if user_order == 'off':
        off = True
    elif user_order == 'report':
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"Money: ${profit}")
    else:
        choice = MENU[user_order]
        resources_enough = check_resources(resources, choice['ingredients'])

        if resources_enough:
            change, product_price = till(choice)
            profit += product_price
            process_payment(change)
            resources = update_resources(choice, resources)


















