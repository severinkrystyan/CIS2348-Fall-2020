"""Name: Krystyan Severin
   PSID: 1916594"""

roster = {}  # Blank dictionary to store roster
jersey_number_1 = int(input('Enter player 1\'s jersey number:\n'))
jersey_rating_1 = int(input('Enter player 1\'s rating:\n'))
jersey_number_2 = int(input('\nEnter player 2\'s jersey number:\n'))
jersey_rating_2 = int(input('Enter player 2\'s rating:\n'))
jersey_number_3 = int(input('\nEnter player 3\'s jersey number:\n'))
jersey_rating_3 = int(input('Enter player 3\'s rating:\n'))
jersey_number_4 = int(input('\nEnter player 4\'s jersey number:\n'))
jersey_rating_4 = int(input('Enter player 4\'s rating:\n'))
jersey_number_5 = int(input('\nEnter player 5\'s jersey number:\n'))
jersey_rating_5 = int(input('Enter player 5\'s rating:\n'))
# Adds Key and Value to Roster dictionary
roster[jersey_number_1] = jersey_rating_1
roster[jersey_number_2] = jersey_rating_2
roster[jersey_number_3] = jersey_rating_3
roster[jersey_number_4] = jersey_rating_4
roster[jersey_number_5] = jersey_rating_5
roster_keys = sorted(roster)  # Creates a sorted list from dictionary keys
print('\nROSTER')
for key in roster_keys:
    print(f'Jersey number: {key}, Rating: {roster[key]}')
while True:
    print('\nMENU')
    print('a - Add player\nd - Remove player\nu - Update player rating')
    print('r - Output players above a rating\no - Output roster\nq - Quit')
    option = input('\nChoose an option:\n')
    if option == 'a':  # Option to add player jersey and rating
        player_jersey = int(input('Enter a new player\'s jersey number:\n'))
        player_rating = int(input('Enter the player\'s rating:\n'))
        roster.update({player_jersey: player_rating})
        roster_keys = sorted(roster)
    elif option == 'd':  # Option to remove player jersey and rating
        remove_player = int(input('Enter a jersey number:\n'))
        del roster[remove_player]
        roster_keys = sorted(roster)  # Resorts the list after element is removed
    elif option == 'u':  # Option to change player rating
        jersey_player = int(input('Enter a jersey number:\n'))
        new_rating = int(input('Enter a new rating for player:\n'))
        roster[jersey_player] = new_rating
        roster_keys = sorted(roster)
    elif option == 'r':  # Option to generate output of players above certain rating
        above_rating = int(input('Enter a rating:\n'))
        print(f'\nABOVE {above_rating}')
        for key in roster_keys:
            if roster[key] > above_rating:
                print(f'Jersey number: {key}, Rating: {roster[key]}')
    elif option == 'o':  # Outputs the roster
        print('\nROSTER')
        for key in roster_keys:
            print(f'Jersey number: {key}, Rating: {roster[key]}')
    elif option == 'q':  # Terminates loop
        break
