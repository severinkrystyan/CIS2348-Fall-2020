"""Name: Krystyan Severin
   PSID: 1916594"""
integer_list = []
numbers = input().split()
for x in numbers:
    x = int(x)  # Convert inputs in list from list to integers
    if x >= 0:
        integer_list.append(x)
        integer_list = sorted(integer_list)  # Sorts list into ascending order
for x in integer_list:
    print(x, end=" ")
