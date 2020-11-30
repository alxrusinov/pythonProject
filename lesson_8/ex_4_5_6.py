class Storage:
    """структура типа {'type': {'model': {'number': 0, 'items': []}}"""

    _items = {}

    def __init__(self, divisions, name):
        self.divisions = divisions
        self.name = name
        self.on_divisions = {i: [] for i in divisions}

    def take_to_storage(self, items):
        for item in items:
            if item.type in self._items:
                if item.model in self._items[item.type]:
                    self._items[item.type][item.model]['items'].append(item)
                    self._items[item.type][item.model]['number'] += 1
                else:
                    self._items[item.type][item.model] = {'number': 1, 'items': [item]}
            else:
                self._items[item.type] = {item.model: {'number': 1, 'items': [item]}}

            item.put_in_storage(self)

    """office_equipments - структура [{'type': '', 'model': '', number: '', division: ''}]"""

    def put_in_division(self, office_equipments):
        for item in office_equipments:
            if item['type'] in self._items and item['model'] in self._items[item['type']] and item['number'] <= \
                    self._items[item['type']][item["model"]]['number']:
                count = 0
                while count < item['number']:
                    current = self._items[item['type']][item["model"]]['items'].pop()
                    self._items[item['type']][item["model"]]['number'] -= 1
                    current.put_in_storage(None)
                    current.put_in_division(item['division'])
                    self.on_divisions[item['division']].append(current)
                    count += 1
            else:
                print(
                    f'{item["type"]} {item["model"]} в количестве {item["number"]} для {item["division"]} нет на складе')
                continue

    @property
    def office_equipment_number(self, office_equipment_type=None, office_equipment_model=None):
        if not office_equipment_type:
            general_number = 0
            for current_type in self._items.keys():
                for current_model in self._items[current_type].keys():
                    general_number += self._items[current_type][current_model]['number']
            else:
                print(f'на складе всего {general_number} едениц техники')
                return general_number
        elif not office_equipment_model:
            if office_equipment_type in self._items:
                number_by_type = 0
                for current_model in self._items[office_equipment_type].keys():
                    number_by_type += self._items[office_equipment_type][current_model]['number']
                else:
                    print(f'на складе {number_by_type} едениц техники типа {office_equipment_type}')
                    return number_by_type
            else:
                print(f'техники типа {office_equipment_type} нет на складе')
        else:
            if office_equipment_type in self._items and office_equipment_model in self._items[office_equipment_type]:
                number_by_model = self._items[office_equipment_type][office_equipment_model]['number']
                print(
                    f'на складе {number_by_model} едениц техники типа {office_equipment_type} модели {office_equipment_model}')
                return number_by_model
            else:
                print(
                    f'на складе техники типа {office_equipment_type} модели {office_equipment_model} нет')

    @property
    def office_equipment_on_storage(self):
        result = {'types': [], 'models': []}
        for office_equipment_type in self._items.keys():
            for office_equipment_model in self._items[office_equipment_type].keys():
                if office_equipment_type not in result['types']:
                    if self._items[office_equipment_type][office_equipment_model]['number']:
                        result['types'].append(office_equipment_type)

                if office_equipment_model not in result['models']:
                    if self._items[office_equipment_type][office_equipment_model]['number']:
                        result['models'].append(office_equipment_model)
        print(f'на складе есть техника типа "{", ".join(result["types"])}" и модели "{", ".join(result["models"])}"')

        return result

    @property
    def office_equipment_in_divisions(self):
        result = dict()
        for key, value in self.on_divisions.items():
            result[key] = len(value)
        return result


class OfficeEquipment:
    type = 'OfficeEquipment'
    _storage = None
    _division = None

    def __init__(self, model, width, height, length, weight):
        self.model = model
        self.width = OfficeEquipment.int_validate(width)
        self.height = OfficeEquipment.int_validate(height)
        self.length = OfficeEquipment.int_validate(length)
        self.weight = weight

    def put_in_storage(self, storage):
        self._storage = storage

    def put_in_division(self, division):
        self._division = division

    @property
    def storage(self):
        return self.storage.get('name')

    @property
    def division(self):
        return self._division

    @staticmethod
    def int_validate(value):
        if type(value) == int:
            return value
        raise ValueError(f'{value} должно быть положительным целым числом')

    def __str__(self):
        return f'{self.type}: model {self.model}, size {self.width}x{self.length}x{self.height}, weight {self.weight}'


class Printer(OfficeEquipment):
    type = 'Printer'

    def __init__(self, model, width, height, length, weight, max_page, page_per_second, colored):
        super().__init__(model, width, height, length, weight)
        self.max_page = Printer.int_validate(max_page)
        self.page_per_second = Printer.int_validate(page_per_second)
        self.colored = colored


class Scanner(OfficeEquipment):
    type = 'Scanner'

    def __init__(self, model, width, height, length, weight, max_dpi):
        super().__init__(model, width, height, length, weight)
        self.max_dpi = Scanner.int_validate(max_dpi)


class Xerox(OfficeEquipment):
    type = 'Xerox'

    def __init__(self, model, width, height, length, weight, max_dpi, cartridge, colored):
        super().__init__(model, width, height, length, weight)
        self.max_dpi = Xerox.int_validate(max_dpi)
        self.slots = Xerox.int_validate(cartridge)
        self.colored = colored


storage = Storage(['Бухгалтерия', 'HR', 'Маркетинг'], 'my_awesome_storage')

printer_1 = Printer(width=200, length=320, height=195, model='Z1200', weight=2300, max_page=150000, page_per_second=1,
                    colored=True)
printer_2 = Printer(width=200, length=320, height=195, model='Z1200', weight=2300, max_page=150000, page_per_second=1,
                    colored=True)
printer_3 = Printer(width=200, length=320, height=195, model='Z1300', weight=1900, max_page=200000, page_per_second=2,
                    colored=True)

scanner_1 = Scanner(model='Sc450', width=245, height=150, length=329, weight=1500, max_dpi=800)
scanner_2 = Scanner(model='Sc450', width=245, height=150, length=329, weight=1500, max_dpi=800)
scanner_3 = Scanner(model='Sc450-m', width=245, height=145, length=329, weight=1500, max_dpi=1200)
scanner_4 = Scanner(model='Sc450-m', width=245, height=145, length=329, weight=1500, max_dpi=1200)

xerox_1 = Xerox(model='xr-500', width=320, length=420, height=255, weight=2500, max_dpi=1200, colored=True, cartridge=2)

office_equipments_pool = [printer_1, printer_2, printer_3, scanner_1, scanner_2, scanner_3, scanner_4, xerox_1]

for i in office_equipments_pool:
    print(i)

print('=' * 54)

storage.take_to_storage(office_equipments_pool)
print(storage.office_equipment_number)
print(storage.office_equipment_on_storage)

print('=' * 54)

storage.put_in_division([{'type': Printer.type, 'model': 'Z1200', 'number': 2, 'division': 'Бухгалтерия'},
                         {'type': Scanner.type, 'model': 'Sc450', 'number': 2, 'division': 'Маркетинг'},
                         {'type': Xerox.type, 'model': 'xr-500', 'number': 12, 'division': 'HR'}])
print(storage.office_equipment_in_divisions)
print(storage.office_equipment_on_storage)
print(storage.office_equipment_number)
xerox_10 = Xerox(model='xr-500', width=320.8, length=420, height=255, weight=2500, max_dpi=1200, colored=True,
                 cartridge=2)
scanner_10 = Scanner(model='Sc450', width=245, height=150, length=329, weight=1500, max_dpi='800')
