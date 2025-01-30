# Coffee
water = 1250
coffee = 120
milk = 750

CAPPUCCINO = {
    'price': 3,
    'water': 250,
    'coffee': 24, 
    'milk': 100
}
ESPRESSO = {
    'price': 3,
    'water': 250,
    'coffee': 24, 
    'milk': 100
}
LATTE = {
    'price': 3,
    'water': 250,
    'coffee': 24, 
    'milk': 100
}

# Machine Functions 
coffee_machine = True
cash_balance = 10
drink_log = ()

penny = 0
nickel = 0
dime = 0
quarter = 0

# Prompt
choice = input('Thank you for choosing Coy\'s Coin Coffee Machine! We proudly serve espresso, latte, and cappuccino.What would you like? ').lower()

while (choice != 'espresso') & (choice != 'latte') & (choice != 'cappuccino'):
    choice = input('Invalid input. Please enter one of the following: espresso, latte, or cappuccino.')