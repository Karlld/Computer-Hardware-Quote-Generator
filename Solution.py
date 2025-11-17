print ('Welcome to the Custom Computer Quote Generator!')

screen_prices = {'a': 50, 'b': 100, 'c': 150}
ram_prices    = {'a': 40, 'b': 80,  'c': 150}
cpu_prices    = {'a': 100, 'b': 200, 'c': 350}
storage_prices = {'a': 30, 'b': 60, 'c': 120}

choices = {}        
total_cost = 0 

print('''
        Please select your screen size: 
                   a. 13" (£50)
                   b. 15" (£100)
                   c. 17" (£150)
      ''')
      
screen = input('Select your option: a, b or c?').lower()
choices['Screen Size'] = screen
total_cost += screen_prices[screen]

 


print('''
         Please select your RAM:
                    a. 8GB (£40)
                    b. 16GB (£80)
                    c. 32GB (£150)
     ''')

ram = input('Select your option: a, b or c?').lower()
choices['RAM'] = screen
total_cost += ram_prices[ram]

print('''
         Please select your CPU clock speed:
                    a. 2.5GHz (£100)
                    b. 3.2GHz (£200)
                    c. 4.0GHz (£350)
     ''')
     
cpu = input('Select your option: a, b or c?').lower()
choices['CPU'] = screen
total_cost += cpu_prices[cpu]

print('''
         Please select your storage:
                    a. 256GB HDD (£30)
                    b. 512GB SSD (£60)
                    c. 1TB SSD (£120)
      ''')
              
storage = input('Select your option: a, b or c?').lower()
choices['Storage'] = screen
total_cost += storage_prices[storage]


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

print(f'\nTOTAL COST: £{total_cost}')
print('------------------------------------------------------------')
