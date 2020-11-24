class Stationery:
    _title = ''

    def draw(self):
        print(f'Запуск отрисовки {self._title}')


class Pen(Stationery):
    _title = 'Ручка'

    def draw(self):
        print(f'О да, это {self._title}!')


class Pencil(Stationery):
    _title = 'Карадаш'

    def draw(self):
        print(f'Это самый быстрый {self._title} на диком западе.')


class Handle(Stationery):
    _title = 'Маркер'

    def draw(self):
        print(f'Это {self._title}, просто {self._title}.')


pen = Pen()
pencil = Pencil()
handle = Handle()

for item in pen, pencil, handle:
    item.draw()

