print ('\nWelcome to the Custom Computer Quote Generator!')

screen_prices = {'a': 50, 'b': 100, 'c': 150}
ram_prices    = {'a': 40, 'b': 80,  'c': 150}
cpu_prices    = {'a': 100, 'b': 200, 'c': 350}
storage_prices = {'a': 30, 'b': 60, 'c': 120}
promos = {'promo-10' : 0.9, 'promo-20' : 0.8, 'promo-30' : 0.7, 'skip' : 1 }
choices = {}        
total_cost = 0 

print('''
        Please select your screen size: 
                   a. 13" (£50)
                   b. 15" (£100)
                   c. 17" (£150)
      ''')
      
while True:      
    screen = input('\nSelect your option: a, b or c?').lower()

    if screen not in screen_prices:
         print('\nInvalid option, please try again!')
         continue 
     
    choices['Screen Size'] = screen
    total_cost += screen_prices[screen]
     
    break

 
print('''
         Please select your RAM:
                    a. 8GB (£40)
                    b. 16GB (£80)
                    c. 32GB (£150)
     ''')
     
while True:
    ram = input('\nSelect your option: a, b or c?').lower()

    if ram not in ram_prices:
         print('\nInvalid option, please try again!')
         continue 
     
    choices['RAM'] = ram
    total_cost += ram_prices[ram]
    
    break

print('''
         Please select your CPU clock speed:
                    a. 2.5GHz (£100)
                    b. 3.2GHz (£200)
                    c. 4.0GHz (£350)
     ''')

while True:     
    cpu = input('\nSelect your option: a, b or c?').lower()

    if cpu not in cpu_prices:
         print('\nInvalid option, please try again!')
         continue 
     
    choices['CPU'] = cpu
    total_cost += cpu_prices[cpu]
   
    break

print('''
         Please select your storage:
                    a. 256GB HDD (£30)
                    b. 512GB SSD (£60)
                    c. 1TB SSD (£120)
      ''')
      
while True:              
    storage = input('\nSelect your option: a, b or c?').lower()
    
    if storage not in storage_prices:
        print('\nInvalid option, please try again!')
        continue 
    
    choices['Storage'] = storage
    total_cost += storage_prices[storage]

    break

print('''
      Do you have a promo code?
      ''')
      
while True:
    promo = input('\nEnter your Promo Code now or type "skip": ').lower()
    
    if promo not in promos:
        print('\nInvalid Promo Code, please try again!')
        continue 
    
  
    if promo == 'promo-30' and total_cost < 600:
        print('\nTotal Cost must be at least £600 for this promotion!')
        continue  
    
 
    choices['Promos'] = promo
    total_cost *= promos[promo]
    
    if promo != 'skip':
        print('\nPromomotion Applied!')
    else:
        print('\nNo Promomotion Applied')
    
    break  

print('\n---------------- Your Custom Computer Quote ----------------')


names = {
    'screen size': {'a': '13"', 'b': '15"', 'c': '17"'},
    'ram': {'a': '8GB', 'b': '16GB', 'c': '32GB'},
    'cpu': {'a': '2.5GHz', 'b': '3.2GHz', 'c': '4.0GHz'},
    'storage': {'a': '256GB HDD', 'b': '512GB SSD', 'c': '1TB SSD'}
}

print(f"\nScreen Size: {names['screen size'][screen]} (£{screen_prices[screen]})")
print(f"RAM: {names['ram'][ram]} (£{ram_prices[ram]})")
print(f"CPU: {names['cpu'][cpu]} (£{cpu_prices[cpu]})")
print(f"Storage: {names['storage'][storage]} (£{storage_prices[storage]})")

print(f'\nTOTAL COST: £{total_cost:.2f}')
print('------------------------------------------------------------')
              
                     
                    
