print('Enter amount of lemon juice (in cups):')  # get user's amount and print them
amount_lemon_juice = float(input())
print('Enter amount of water (in cups):')
amount_water = float(input())
print('Enter amount of agave nectar (in cups):')
amount_agave = float(input())
print('How many servings does this make?')
amount_servings = float(input())


print('\nLemonade ingredients - yields', ('{:.2f}'.format(amount_servings)), 'servings')  # format to decimals
print('{:.2f}'.format(amount_lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(amount_water), 'cup(s) water')
print('{:.2f}'.format(amount_agave), 'cup(s) agave nectar')

print('\nHow many servings would you like to make?')  # calculate servings
amount_servings_required = float(input())
print('\nLemonade ingredients - yields', '{:.2f}'.format(amount_servings_required), 'servings')
print('{:.2f}'.format((amount_lemon_juice*amount_servings_required)/amount_servings), 'cup(s) lemon juice')
print('{:.2f}'.format((amount_water*amount_servings_required)/amount_servings), 'cup(s) water')
print('{:.2f}'.format((amount_agave*amount_servings_required)/amount_servings), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', ('{:.2f}'.format(amount_servings_required)), 'servings')  # format servings
print('{:.2f}'.format(amount_lemon_juice*amount_servings_required/amount_servings/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(amount_water*amount_servings_required/amount_servings/16), 'gallon(s) water')
print('\n{:.2f}'.format(amount_agave*amount_servings_required/amount_servings/16), 'gallon(s) agave nectar')
