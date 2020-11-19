language_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def replace_in_string(string, dictionary):
    source_list = string.split(' - ')
    source_list[0] = dictionary[source_list[0]]
    return ' - '.join(source_list)


def write_to(file_for_write, data):
    with open(file_for_write, 'a', encoding='utf-8') as target:
        target.write(data)


def parse_source_file(source_file, target_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as source:
            for string in source:
                write_to(target_file, replace_in_string(string, language_dict))
    except FileNotFoundError as err:
        print(err)


parse_source_file('file_4.txt', 'new_file_4.txt')
