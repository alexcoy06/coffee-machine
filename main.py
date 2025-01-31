# Coffee
drink_choices = {
    'resources': {
        'coffee': 120,
        'milk': 750,
        'water': 1250
    },
    'cappuccino': {
        'coffee': 24,
        'milk': 100,
        'water': 250,
        'cost': 3
    },
    'espresso': {
        'coffee': 18,
        'milk': 0,
        'water': 50,
        'cost': 1.5
    },
    'latte': {
        'coffee': 24,
        'milk': 150,
        'water': 200,
        'cost': 2.5
    }
}


# Machine Functions 
machine_running = True
cash_balance = 0
machine_log = []

money = {
    'quarters': 0,
    'dimes': 0,
    'nickels': 0,
    'pennies': 0
}


# Coded Function
def report(resources=drink_choices):
    for resource, amount in resources['resources'].items():
        if resource == 'coffee':
            print(f'{resource.capitalize()}: {amount}gm')
        else:
            print(f'{resource.capitalize()}: {amount}ml')
    print(f'Cash Balance: {cash_balance}\nMachine Log: {", ".join(machine_log)}')
    
def update_resources(choice, drink_choices=drink_choices):
    drink = drink_choices[choice]
    resources = drink_choices['resources']
    drink_failed = 0
    
    for resource in resources:
        if resources[resource] < drink[resource]:
            drink_failed = 1
            print(f'Sorry, not enough {resource}.')
                
            
    if drink_failed == 0:
        resources['coffee'] -= drink['coffee']
        resources['milk'] -= drink['milk']
        resources['water'] -= drink['water']
        machine_log.append(choice)
    else:
        machine_log.append(choice + '.failed')
    return drink_choices, machine_log

def buy_coffee(choice, money=money, cash_balance=cash_balance):
    cost = drink_choices[choice]['cost']
    paid = 0
    change = -1
    not_enough_money = True
    
    while not_enough_money:
        count = {
            'quarters': 0,
            'dimes': 0,
            'nickels': 0,
            'pennies': 0    
        }
        
        print(f'Your {choice.capitalize()} will cost ${cost:.2f}. Please insert coins.')
        for coin in money:
            count[coin] = int(input(f'How many {coin}: '))
        
        paid =  (0.1 *count['dimes']) + (0.05 * count['nickels']) + (0.01 * count['pennies']) + (0.25 * count['quarters'])
            
        if paid >= cost:
            money[coin] += count[coin] # plan to come back and do more with this
            change = paid - cost
            cash_balance += cost - change
            print(f'Your change is ${change:.2f}')
            not_enough_money = False
            
        else:
            attempt = input(f'Insufficient funds, "try again" or "cancel": ').lower()
            if attempt == 'cancel':
                not_enough_money = False
            elif attempt == 'try again':
                pass
            else:
                print('Wrong input.')
            
    return money, cash_balance


#Machine Operation
while machine_running:
    # Prompt
    choice = input('Thank you for choosing Coy\'s Coin Coffee Machine! We proudly serve espresso, latte, and cappuccino.What would you like? ').lower()
    
    # Input Controls 
    while (choice != 'espresso') & (choice != 'latte') & (choice != 'cappuccino') & (choice != 'report') & (choice != 'off'):
        choice = input('Invalid input. Please enter one of the following: espresso, latte, or cappuccino.')
    
    if choice == 'off':
        machine_running = False
    elif choice == 'report':
        report()
        machine_log.append(choice)
    else:
        drink_choices, machine_log = update_resources(choice)
        
    if (choice in drink_choices) & ('.failed' not in machine_log[-1]):
        money, cash_balance = buy_coffee(choice)
        
    # Add 'out of service' task did not require but i want to at some point