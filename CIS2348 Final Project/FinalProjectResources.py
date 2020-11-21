"""Name: Krystyan Severin
   PSID: 1916594"""
import csv


def past_due_checker(today, due):
    current_date = (today.split('/'))
    serv_date = (due.split('/'))
    current_date = [int(number) for number in current_date]
    serv_date = [int(number) for number in serv_date]
    if current_date[2] > serv_date[2]:
        return True
    elif current_date[2] < serv_date[2]:
        return False
    elif current_date[0] > serv_date[0]:
        return True
    elif current_date[0] < serv_date[0]:
        return False
    elif current_date[0] == serv_date[0]:
        if current_date[1] > serv_date[1]:
            return True
        elif current_date[1] < serv_date[1]:
            return False


def get_data():
    main_inventory = []
    # ManufacturerList.csv
    manufactures = open('ManufacturerList.csv')
    manufactures_read = csv.reader(manufactures)
    for manufacture in manufactures_read:
        main_inventory.append(manufacture)
    manufactures.close()
    # PriceList.csv
    prices = open('PriceList.csv')
    prices_read = csv.reader(prices)
    price_list = [price for price in prices_read]
    # Finds correct ID and appends price
    for idx, inventory in enumerate(main_inventory):
        for ind, price in enumerate(price_list):
            if price[0] == inventory[0]:
                main_inventory[idx].insert(3, price_list[ind][1])
    prices.close()
    # ServiceDatesList.csv
    dates = open('ServiceDatesList.csv')
    dates_read = csv.reader(dates)
    date_list = [date for date in dates_read]
    # Find correct ID and appends service date
    for idx, inventory in enumerate(main_inventory):
        for ind, date in enumerate(date_list):
            if date[0] == inventory[0]:
                main_inventory[idx].insert(4, date_list[ind][1])
    dates.close()
    for idx, invent in enumerate(main_inventory):
        for ind, x in enumerate(invent):
            main_inventory[idx][ind] = x.strip().capitalize()
    return main_inventory
