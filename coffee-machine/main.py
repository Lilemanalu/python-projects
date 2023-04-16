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
    },
    "americano": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
        },
        "cost": 2.0,
    },
    "mocha": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 18,
            "chocolate": 25,
        },
        "cost": 3.5,
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "chocolate": 50,
}

def print_report():
    """Prints the current state of resources and profit."""
    print("Current resources:")
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")
    print(f"Profit: ${profit}")

def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to fulfill the order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(drink_cost):
    """Processes the payment for the order."""
    print("Please insert coins.")
    total = 0
    coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
    for coin in coins:
        total += int(input(f"How many {coin}?: ")) * coins[coin]
    if total < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(total - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True

def make_drink(drink_name, order_ingredients):
    """Makes the drink and deducts the required resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/americano/mocha): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                if process_payment(drink["cost"]):
                    make_drink(choice, drink["ingredients"])
        else:
            print("Sorry, we don't have that option. Please try again.")
