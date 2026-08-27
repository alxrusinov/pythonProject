class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_as_int_extract(cls, date):
        try:
            if cls.date_validate(date):
                return tuple(int(x) for x in date.split('-'))
        except ValueError as error:
            print(error)

    @staticmethod
    def date_validate(date):
        day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dates = [int(x) for x in date.split('-')]
        date_is_valid = False

        try:
            if len(dates) != 3:
                raise ValueError('Incorrect date format')
        except ValueError as error:
            print(error)
        else:
            try:
                day = int(dates[0])
                month = int(dates[1])
                year = int(dates[2])
                if 1 > month or month > 12:
                    raise ValueError('month is incorrect')
                if 1 > day or day > day_in_month[month - 1]:
                    raise ValueError('day is incorrect')
                if year < 0:
                    raise ValueError('year is incorrect')
            except ValueError as error:
                print(error)
            else:
                date_is_valid = True
        finally:
            return date_is_valid


date_1 = Date('11-11-2020')
date_2 = Date('32-02-1212')
date_3 = Date('12-12-1212')
date_4 = Date('13-13-1313')
date_5 = Date('13-12-1313')

print(date_1.date)
print(Date.date_as_int_extract(date_2.date))
print(Date.date_as_int_extract(date_3.date))
print(date_1.date_validate(date_4.date))
print(Date.date_validate(date_5.date))
