"""Name: Krystyan Severin
   PSID: 1916594"""
months = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7',
          'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}

with open("inputDates.txt", "r") as f:
    file = f.readlines()
    print("--")
    for line in file:
        date = line.replace("\n", "")
        # Resets variables for each iteration
        month = ""
        year = ""
        day = ""
        # Checks length first to ensure general format//Short hand dates do not exceed 8 characters
        if len(date[::-1]) > 10:
            # Checks to see if comma is included and that the year has four digits
            if date[-6] == ',' and len(date[-4:]) == 4:
                for mon in months:
                    if date.find(mon) != -1:
                        month = months[mon]
                year = date[-4:]
                day = date[-8:-6].replace(" ", "")  # Removes white space in case of single digit in day
                if month:  # Makes sure the month variable is not empty
                    print(f'{month}/{day}/{year}')
    f.close()
print("--")
