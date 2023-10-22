import re
import json
from prettytable import PrettyTable, ALL
from datetime import datetime

pattern = r'^[+-]\s\d+[ec]\s+\d+$'
my_table = PrettyTable(['Time', 'Notes', '2Eur', '1eur', '50 c', '20 c', '10 c', '5 c', '2 c', '1 c', 'Total'])
my_table.hrules = ALL
money = {
    'notes': 0,
    'coins_2eur': 0,
    'coins_1eur': 0,
    'coins_50c': 0,
    'coins_20c': 0,
    'coins_10c': 0,
    'coins_5c': 0,
    'coins_2c': 0,
    'coins_1c': 0,
    'total': 0
}

while True:
    command = input()
    if command == 'import':
        with open('C:/Users/gosha/VisualStudioProjects/python_programs/backup.json', 'r') as backup:
            money = json.load(backup)
        continue
    if command == '!':
        my_table = PrettyTable(['Time', 'Notes', '2Eur', '1eur', '50 c', '20 c', '10 c', '5 c', '2 c', '1 c', 'Total'])
        my_table.add_row([datetime.now(), round(money['notes'], 2), round(money['coins_2eur'], 2), round(money['coins_1eur'], 2), round(money['coins_50c'], 2), round(money['coins_20c'], 2), round(money['coins_10c'], 2), round(money['coins_5c'], 2), round(money['coins_2c'], 2), round(money['coins_1c'], 2), round(money['total'], 2)])
        print(my_table)
        continue
    match = re.search(pattern, command)
    if match:
        command = command.split()
        if command[0] == '+':
            if command[1] in ['50e', '20e', '10e', '5e']:
                money['notes'] += round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '2e':
                money['coins_2eur'] += round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '1e':
                money['coins_1eur'] += round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '50c':
                money['coins_50c'] += round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '20c':
                money['coins_20c'] += round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '10c':
                money['coins_10c'] += round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '5c':
                money['coins_5c'] += round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '2c':
                money['coins_2c'] += round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '1c':
                money['coins_1c'] += round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            else:
                print(f'Wrong face value {command[1]}')
                continue
            with open('C:/Users/gosha/VisualStudioProjects/python_programs/backup.json', 'w', encoding='utf-8') as backup:
                total = sum((round(money['notes'], 2), round(money['coins_2eur'], 2), round(money['coins_1eur'], 2), round(money['coins_50c'], 2), round(money['coins_20c'], 2), round(money['coins_10c'], 2), round(money['coins_5c'], 2), round(money['coins_2c'], 2), round(money['coins_1c'], 2)))
                money['total'] = round(total, 2)
                backupJSON = json.dumps(money, indent=4)
                backup.write(backupJSON)
        elif command[0] == '-':
            if command[1] in ['50e', '20e', '10e', '5e']:
                money['notes'] -= round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '2e':
                money['coins_2eur'] -= round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '1e':
                money['coins_1eur'] -= round(float(command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '50c':
                money['coins_50c'] -= round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '20c':
                money['coins_20c'] -= round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '10c':
                money['coins_10c'] -= round(float('0.' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '5c':
                money['coins_5c'] -= round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '2c':
                money['coins_2c'] -= round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            elif command[1] == '1c':
                money['coins_1c'] -= round(float('0.0' + command[1][:-1]) * float(command[-1]), 2)
            else:
                print(f'Wrong face value {command[1]}')
                continue
            with open('C:/Users/gosha/VisualStudioProjects/python_programs/backup.json', 'w', encoding='utf-8') as backup:
                total = sum((round(money['notes'], 2), round(money['coins_2eur'], 2), round(money['coins_1eur'], 2), round(money['coins_50c'], 2), round(money['coins_20c'], 2), round(money['coins_10c'], 2), round(money['coins_5c'], 2), round(money['coins_2c'], 2), round(money['coins_1c'], 2)))
                money['total'] = round(total, 2)
                backupJSON = json.dumps(money, indent=4)
                backup.write(backupJSON)
    else:
        print(f'Wrong command [{command}]')
