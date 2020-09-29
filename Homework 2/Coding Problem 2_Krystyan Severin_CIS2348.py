"""Name: Krystyan Severin
   PSID: 1916594"""
months = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7',
          'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}
month = ""
day = ""
year = ""
date = input("Please enter date: ")
# Checks to see if comma is included and that the year has four digits
if date[-6] == ',' and len(date[-4:]) == 4:
    for mon in months:
        if date.find(mon) != -1:
            month = months[mon]
    year = date[-4:]
    day = date[-8:-6].replace(" ", "")  # Removes wipe space in case of single digit in day
    print(f'{month}/{day}/{year}')
