index = 1
goods = []

while True:
    name = input('введите наименование товара ')

    if name == '':
        break

    price = int(input('введите цену товара '))
    quantity = int(input('введите количество товара '))
    unit = input('введите единицы измерения ')

    goods_item = (index, {'наименование': name, 'цена': price, 'количество': quantity, 'ед': unit})
    goods.append(goods_item)
    index += 1

print(goods)

analytics = {
    'наименование': [],
    'цена': [],
    'количество': [],
    'ед': []
}

for item in goods:
    goods_item = item[1]
    if not (goods_item['наименование'] in analytics['наименование']):
        analytics['наименование'].append(goods_item['наименование'])
    if not (goods_item['цена'] in analytics['цена']):
        analytics['цена'].append(goods_item['цена'])
    if not (goods_item['количество'] in analytics['количество']):
        analytics['количество'].append(goods_item['количество'])
    if not (goods_item['ед'] in analytics['ед']):
        analytics['ед'].append(goods_item['ед'])

print(analytics)
