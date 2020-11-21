"""Name: Krystyan Severin
   PSID: 1916594"""
from operator import itemgetter
import csv
import datetime
import FinalProjectResources

if __name__ == '__main__':
    """ Full Inventory Creation """
    full_inventory = [invent for invent in FinalProjectResources.get_data()]
    full_inventory.sort(key=itemgetter(1, 2))
    inventory_file = open('FullInventory.csv', mode='w', newline='')
    inventory_write = csv.writer(inventory_file, delimiter=',')
    inventory_write.writerows(full_inventory)
    inventory_file.close()
    """ Item Type Inventory Creation """
    item_type = [item for item in FinalProjectResources.get_data()]
    item_type.sort(key=itemgetter(0))
    item_names = []
    for i, names in enumerate(item_type):
        if names[2] not in item_names:
            item_names.append(names[2])
    for names in item_names:
        for item in item_type:
            item_file = open(names.capitalize()+'Inventory.csv', mode='a', newline='')
            if item[2] == names:
                item.remove(names)
                item_write = csv.writer(item_file, delimiter=',')
                item_write.writerow(item)
                item_file.close()
    """ Past Service Date Inventory Creation """
    past_service = [date for date in FinalProjectResources.get_data()]
    past_service.sort(key=lambda date: datetime.datetime.strptime(date[4], "%m/%d/%Y"))
    todays = datetime.date.today()
    today_date = todays.strftime("%m/%d/%Y")
    for idx, item in enumerate(past_service):
        status = FinalProjectResources.past_due_checker(today_date, item[4])
        if status:
            with open('PastServiceDateInventory.csv', mode='a', newline='') as past_due:
                past_due_list = csv.writer(past_due, delimiter=',')
                past_due_list.writerow(item)
    """ Damaged Inventory Creation """
    damaged = [damage for damage in FinalProjectResources.get_data()]
    damaged.sort(key=itemgetter(3))
    for idx, item in enumerate(damaged):
        if item[5]:
            with open('DamagedInventory.csv', mode='a', newline='') as damaged:
                del item[5]
                damage_list = csv.writer(damaged, delimiter=',')
                damage_list.writerow(item)
