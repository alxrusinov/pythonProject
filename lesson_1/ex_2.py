time_sec = int(input('введите время в секундах '))

sec_in_min = 60
sec_in_hour = 3600

print(f'вы ввели {time_sec // sec_in_hour:02d}:{time_sec // sec_in_min:02d}:{time_sec % sec_in_min:02d}')
