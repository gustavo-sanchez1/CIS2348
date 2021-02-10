import math
paint_colors_prices = {  # create dictionary with colors and prices
    'red': 35,
    'blue': 75,
    'green': 23
}
print('Enter wall height (feet):')  # get user's input and print them
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())
wall_area = wall_height*wall_width  # calculate area and paint needed
print('Wall area:', wall_area, 'square feet')
paint_needed = wall_area/350
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')  # format numbers
cans_needed = math.ceil(paint_needed)

print('Cans needed:', cans_needed, 'can(s)')  # use the dictionary
color = input('\nChoose a color to paint the wall:')
print("\nCost of purchasing " + color + " paint: $" + str(paint_colors_prices[color]))
