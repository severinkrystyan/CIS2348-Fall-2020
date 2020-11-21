"""Name: Krystyan Severin
   PSID: 1916594"""
import datetime
import FinalProjectResources


def init():
    main_inventory = FinalProjectResources.get_data()
    # Creates references for manufacture name and item type
    manufacture_names = []
    for manufacture in main_inventory:
        if manufacture[1] not in manufacture_names:
            manufacture_names.append(manufacture[1])
    item_names = []
    for item in main_inventory:
        if item[2] not in item_names:
            item_names.append(item[2])
    return main_inventory, manufacture_names, item_names


def multiple_items(found):
    if len(found) == 0:
        return 'Null'
    # If multiple items are found the most expensive is chosen
    elif len(found) > 1:
        prices = []
        for item in found:
            prices.append(int(item[3]))
        most_expensive = max(prices)
        for price in found:
            if price[3] == str(most_expensive):
                print(f'Your item is: ID- {price[0]} | Name- {price[1]} | Type- {price[2]} '
                      f'| Price- ${price[3]}')
                return price
    elif len(found) == 1:
        for item in found:
            print(f'Your item is: ID- {item[0]} | Name- {item[1]} | Type- {item[2]} | Price- ${item[3]}')
            return found


def search_inventory(inventory, words, items, manufactures):
    today = datetime.date.today()
    today_date = today.strftime("%m/%d/%Y")
    found = False
    manufacture = ''
    category = ''
    manufacture_count = 0
    category_count = 0
    for word in words:
        if word in manufactures:
            manufacture = word
            found = True
            manufacture_count += 1
        elif word in items:
            category = word
            found = True
            category_count += 1
    if not found:
        return 'Null'
    # Checks to make sure only one brand and one type was searched for and not (ex. Apple Dell Laptop)
    elif manufacture_count > 1 or category_count > 1:
        return 'Null'
    elif found:
        # Both brand and type searched (ex. Apple Laptop)
        if manufacture and category:
            items_found = []
            for idx, invent in enumerate(inventory):
                if invent[1] == manufacture and invent[2] == category and invent[5] != 'Damaged':
                    if not FinalProjectResources.past_due_checker(today_date, invent[4]):
                        items_found.append(invent)
            product = multiple_items(items_found)
            if product == 'Null':
                return 'Null'
            else:
                # Searching for similar items
                similar_items = []
                for idx, invent in enumerate(inventory):
                    if invent[2] == category and invent[0] != product[0][0] and invent[5] != 'Damaged':
                        if not FinalProjectResources.past_due_checker(today_date, invent[4]):
                            similar_items.append(invent)
                if similar_items:
                    print('\nYou may also consider')
                    multiple_items(similar_items)
                else:
                    print('\nNo similar items found')
        else:
            return 'Null'


if __name__ == '__main__':
    inventory_full = init()
    manufacture_list = inventory_full[1]
    item_type_list = inventory_full[2]
    print('Enter \'q\' to exit')
    user_input = input('Please enter manufacturer and item type: ')
    while user_input != 'q':
        queries = user_input.split()
        queries = [word.capitalize() for word in queries]
        search = search_inventory(inventory_full[0], queries, item_type_list, manufacture_list)
        if user_input == 'q':
            break
        elif search == 'Null':
            print('No such item found')
        user_input = input('\nPlease enter manufacturer and item type: ')
