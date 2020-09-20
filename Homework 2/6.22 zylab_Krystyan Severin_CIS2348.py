"""Name: Krystyan Severin
   PSID: 1916594"""
# First equation variables
var_A = int(input())
var_B = int(input())
var_C = int(input())
# Second equation variables
var_D = int(input())
var_E = int(input())
var_F = int(input())
# Solution variables
first_x = 0
second_y = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        if (var_A * x) + (var_B * y) == var_C and (var_D * x) + (var_E * y) == var_F:
            first_x = x
            second_y = y
if first_x != 0 and second_y != 0:
    print(first_x, second_y)
else:
    print('No solution')
