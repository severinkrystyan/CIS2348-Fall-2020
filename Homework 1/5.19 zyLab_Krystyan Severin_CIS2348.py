"""Name: Krystyan Severin
   PSID: 1916594"""
print('Davy\'s auto shop services')
print('Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service'}
first_service = input('Select first service:\n')
sec_service = input('Select second service:\n')
print('\nDavy\'s auto shop invoice')
if first_service == '-':  # Allows user to enter no service
    print(f'\nService 1: {services[first_service]}')
    print(f'Service 2: {sec_service}, ${services[sec_service]}\n')
    print(f'Total: ${services[sec_service]}')
elif sec_service == '-':  # Allows user to enter no service
    print(f'\nService 1: {first_service}, ${services[first_service]}')
    print(f'Service 2: {services[sec_service]}\n')
    print(f'Total: ${services[first_service]}')
else:
    print(f'\nService 1: {first_service}, ${services[first_service]}')
    print(f'Service 2: {sec_service}, ${services[sec_service]}')
    print(f'\nTotal: ${(services[first_service] + services[sec_service])}')
