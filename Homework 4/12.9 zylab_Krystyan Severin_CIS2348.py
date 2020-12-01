"""Name: Krystyan Severin
   PSID: 1916594"""

ages = []  # List to store user ages
names = []  # List to store names
user_info = input()
while user_info != '-1':
    user_data = user_info.split()
    try:
        names.append(user_data[0])
        ages.append(int(user_data[1]))
    except ValueError:
        del user_data[1]
        ages.append(0)
    user_info = input()

for name, age in zip(names, ages):
    if age != 0:
        print(f'{name} {age+1}')
    elif age == 0:
        print(f'{name} {age}')
