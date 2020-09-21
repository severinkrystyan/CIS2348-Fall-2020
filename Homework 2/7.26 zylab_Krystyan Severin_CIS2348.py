"""Name: Krystyan Severin
   PSID: 1916594"""


def exact_change(user_total):
    coins = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    if user_total >= 0:  # Ensures that user_total is not a negative
        num_dollars = user_total // coins['dollars']
        user_total -= num_dollars * coins['dollars']
    if user_total >= 0:
        num_quarters = user_total // coins['quarters']
        user_total -= num_quarters * coins['quarters']
    if user_total >= 0:
        num_dimes = user_total // coins['dimes']
        user_total -= num_dimes * coins['dimes']
    if user_total >= 0:
        num_nickels = user_total // coins['nickels']
        user_total -= num_nickels * coins['nickels']
    if user_total >= 0:
        num_pennies = user_total // coins['pennies']
        user_total -= num_pennies * coins['pennies']
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

# Main Program


if __name__ == '__main__':
    total = int(input())
    if total <= 0:
        print('no change')
    else:
        amount = exact_change(total)
        if amount[0] != 0 and amount[0] == 1:
            print(amount[0], 'dollar')
        elif amount[0] > 1:
            print(amount[0], 'dollars')
        if amount[1] != 0 and amount[1] == 1:
            print(amount[1], 'quarter')
        elif amount[1] > 1:
            print(amount[1], 'quarters')
        if amount[2] != 0 and amount[2] == 1:
            print(amount[2], 'dime')
        elif amount[2] > 1:
            print(amount[2], 'dimes')
        if amount[3] != 0 and amount[3] == 1:
            print(amount[3], 'nickel')
        elif amount[3] > 1:
            print(amount[3], 'nickels')
        if amount[4] != 0 and amount[4] == 1:
            print(amount[4], 'penny')
        elif amount[4] > 1:
            print(amount[4], 'pennies')
