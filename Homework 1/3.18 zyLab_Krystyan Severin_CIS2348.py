"""Name: Krystyan Severin
   PSID: 1916594"""
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = width * height
print(f'Wall area: {area} square feet')
paint_needed = area/350
print('Paint needed: {0:.2f} gallons'.format(paint_needed))
can_needed = round(paint_needed)
print(f'Cans needed: {can_needed} can(s)')

wall_color = input('\nChoose a color to paint the wall:\n').lower()  # Prevents case sensitivity
colors = {'red': 35, 'blue': 25, 'green': 23}
price = colors[wall_color] * can_needed
print(f'Cost of purchasing {wall_color} paint: ${price}')
