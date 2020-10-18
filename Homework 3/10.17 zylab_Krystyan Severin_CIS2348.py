"""Name: Krystyan Severin
   PSID: 1916594"""


class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity  # Calculates cost of item based on quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}')
        return cost


if __name__ == "__main__":
    # Takes user inputs
    print('Item 1')
    item_name_1 = input('Enter the item name:\n')
    item_price_1 = int(input('Enter the item price:\n'))
    item_quantity_1 = int(input('Enter the item quantity:\n'))
    # Creates instance of class ItemToPurchase
    item_1 = ItemToPurchase(item_name_1, item_price_1, item_quantity_1)
    # Takes user inputs
    print('\nItem 2')
    item_name_2 = input('Enter the item name:\n')
    item_price_2 = int(input('Enter the item price:\n'))
    item_quantity_2 = int(input('Enter the item quantity:\n'))
    # Creates another instance of class ItemToPurchase
    item_2 = ItemToPurchase(item_name_2, item_price_2, item_quantity_2)
    # Produces total cost output
    print('\nTOTAL COST')
    cost_1 = item_1.print_item_cost()
    cost_2 = item_2.print_item_cost()
    print(f'\nTotal: ${cost_1+cost_2}')
