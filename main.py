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
        'water': 250
    },
    'espresso': {
        'coffee': 18,
        'milk': 0,
        'water': 50
    },
    'latte': {
        'coffee': 24,
        'milk': 150,
        'water': 200
    }
}


# Machine Functions 
machine_running = True
cash_balance = 10
machine_log = []

penny = 0
nickel = 0
dime = 0
quarter = 0


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

def buy_coffee():
    return


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
        machine_log.append(choice)
        report()
    else:
        drink_choices, machine_log = update_resources(choice)
        
    
        