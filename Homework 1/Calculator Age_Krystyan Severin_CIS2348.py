"""Name: Krystyan Severin
   PSID: 1916594"""
current_year = int(input('Please enter the current year(yyyy): '))
current_month = int(input('Please enter the current month: '))
current_day = int(input('Please enter the current day: '))
birth_year = int(input('Please enter your birth year(yyyy): '))
birth_month = int(input('Please enter your birth month: '))
birth_day = int(input('Please enter your birth day: '))
age = current_year - birth_year
print('\nBirthday Calculator')
print('Current Day')
print(f'Month: {current_month}\nDay: {current_day}\nYear: {current_year}')
print('Birthday')
print(f'Month: {birth_month}\nDay: {birth_day}\nYear: {birth_year}')
if birth_month > current_month:
    age -= 1
    print(f'\nYou are {age} years old.')
elif birth_month == current_month:
    if birth_day > current_day:
        age -= 1
        print(f'\nYou are {age} years old.')
    elif birth_day == current_day:
        print(f'\nHappy Birthday. You are {age} years old.')
    else:
        print(f'\nYou are {age} years old.')
else:
    print(f'\nYou are {age} years old.')
