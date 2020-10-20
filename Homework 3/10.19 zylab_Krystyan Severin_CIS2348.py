"""Name: Krystyan Severin
   PSID: 1916594"""


class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = int(price)
        self.item_quantity = int(quantity)
        self.item_description = description

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity  # Calculates cost of item based on quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}')
        return cost

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}, {self.item_quantity} oz.')


class ShoppingCart:
    def __init__(self, name='none', date='January 1, 2016'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for idx, instance in enumerate(self.cart_items):
            if self.cart_items[idx].item_name == item_name:
                self.cart_items.pop(idx)
                found = True
        if not found:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, name, quantity):
        found = False
        for idx, instance in enumerate(self.cart_items):
            if self.cart_items[idx].item_name == name:
                self.cart_items[idx].item_quantity = quantity
        if not found:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        item_count = 0
        for idx, instance in enumerate(self.cart_items):
            item_count += self.cart_items[idx].item_quantity
        return item_count

    def get_cost_of_cart(self):
        total_cost = 0
        for idx, instance in enumerate(self.cart_items):
            total_cost += self.cart_items[idx].item_quantity * self.cart_items[idx].item_price
        return total_cost

    def print_total(self):
        if self.cart_items:
            print('\nOUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}\n')
            for idx, instance in enumerate(self.cart_items):
                name = self.cart_items[idx].item_name
                quantity = self.cart_items[idx].item_quantity
                price = self.cart_items[idx].item_price
                print(f'{name} {quantity} @ ${price} = ${price*quantity}')
            print(f'\nTotal: ${self.get_cost_of_cart()}')
        else:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print('Number of Items: 0')
            print('\nSHOPPING CART IS EMPTY\n')
            print('Total: $0')

    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        print('Item Descriptions')
        for idx, instance in enumerate(self.cart_items):
            print(f'{self.cart_items[idx].item_name}: {self.cart_items[idx].item_description}')


def print_menu(option, shopping_cart):
    while True:
        if option == 'a':
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            # Creates instance of ItemToPurchase class
            purchase_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(purchase_item)
            print('\nMENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit\n')
        elif option == 'r':
            print('REMOVE ITEM FROM CART')
            item_remove = input('Enter name of item to remove:\n')
            shopping_cart.remove_item(item_remove)
            print('\nMENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit\n')
        elif option == 'c':
            print('CHANGE ITEM QUANTITY')
            item_name = input('Enter the item name:\n')
            item_quantity = int(input('Enter the new quantity:\n'))
            shopping_cart.modify_item(item_name, item_quantity)
            print('\nMENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit\n')
        elif option == 'i':
            shopping_cart.print_descriptions()
            print('\nMENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit\n')
        elif option == 'o':
            shopping_cart.print_total()
            print('\nMENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit\n')
        elif option == 'q':
            print()  # Blank lines for zylab format
            break
        else:
            print()  # Blank lines for zylab format
        option = input('Choose an option:')


if __name__ == "__main__":
    cus_name = input('Enter customer\'s name:\n')
    day = input('Enter today\'s date:\n')
    print(f'\nCustomer name: {cus_name}')
    print(f"Today's date: {day}")
    # Creates instance of ShoppingCart class
    cart = ShoppingCart(cus_name, day)

    print('\nMENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit\n')
    command = input('Choose an option:')
    # Calls print_menu function with command chosen
    print_menu(command, cart)
