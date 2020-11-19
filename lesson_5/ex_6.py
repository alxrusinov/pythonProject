from re import findall


def number_parse(string):
    return [float(i) for i in findall(r'\d+', string)]


def sum_number_from_string(string):
    return sum(number_parse(string))


def get_dict_from_source(source_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as source:
            result = dict()

            for key, val in [item.split(':') for item in source.readlines()]:
                result[key] = result[key] + sum_number_from_string(
                    val) if key in result else sum_number_from_string(val)
            else:
                print(result)
    except FileNotFoundError as error:
        print(error)
    except ValueError as value_error:
        print(value_error)


get_dict_from_source('file_6.txt')
