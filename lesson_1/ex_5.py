proceeds = int(input('укажите выручку '))
costs = int(input('укажите издержки '))

if costs > proceeds:
    print(f'Получен убыток')
else:
    print(f'получена прибыль')
    profit = (proceeds - costs) / proceeds
    employees = int(input('введите численность сотрудников '))
    profit_on_employee = proceeds / employees
    print(f'рентабельность {profit:.4f}, прибыль на одного сотрудника {profit_on_employee:.4f}')
