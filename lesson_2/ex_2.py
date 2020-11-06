data_list = []

while True:
    item = input('введите очередной элемент списка ')
    if item != '':
        data_list.append(item)
    else:
        break

print(f'original list {data_list}')

len_data_list = len(data_list)

for i in range(len_data_list):
    if len_data_list == 0:
        break
    if i % 2 == 0:
        continue
    else:
        data_list[i - 1], data_list[i] = data_list[i], data_list[i - 1]

print(f'transformed list {data_list}')
