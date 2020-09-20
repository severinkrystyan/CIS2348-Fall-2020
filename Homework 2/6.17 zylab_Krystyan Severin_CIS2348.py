"""Name: Krystyan Severin
   PSID: 1916594"""
initial_password = input()
password = ''
for letter in initial_password:
    if letter == 'i':
        password += '!'
    elif letter == 'a':
        password += '@'
    elif letter == 'm':
        password += 'M'
    elif letter == 'B':
        password += '8'
    elif letter == 'o':
        password += '.'
    else:
        password += letter
password += 'q*s'
print(password)
