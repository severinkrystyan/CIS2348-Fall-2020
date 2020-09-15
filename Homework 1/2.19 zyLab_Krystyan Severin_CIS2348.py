"""Name: Krystyan Severin
   PSID: 1916594"""
# Part 1
lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print('\nLemonade ingredients - yields {0:.2f} servings'.format(servings))
print('{0:.2f} cup(s) lemon juice\n{1:.2f} cup(s) water'.format(lemon, water))
print('{0:.2f} cup(s) agave nectar'.format(agave_nectar))
# Part 2
make_servings = float(input('\nHow many servings would you like to make?\n'))
print('\nLemonade ingredients - yields {0:.2f} servings'.format(make_servings))
lemon = make_servings * (2/6)   # Finds how much one cup would be
water = make_servings * (16/6)
agave_nectar = make_servings * (2.5/6)
print('{0:.2f} cup(s) lemon juice\n{1:.2f} cup(s) water'.format(lemon, water))
print('{0:.2f} cup(s) agave nectar'.format(agave_nectar))
# Part 3
print('\nLemonade ingredients - yields {0:.2f} servings'.format(make_servings))
print('{0:.2f} gallon(s) lemon juice\n{1:.2f} gallon(s) water'.format(lemon/16, water/16)) # Dividing by 16 converts from cups to gallons
print('{0:.2f} gallon(s) agave nectar'.format(agave_nectar/16))
