def salary_statement_parser(salary_statement):
    with open(salary_statement, 'r', encoding='utf-8') as salaries:
        data = [i.split() for i in salaries.readlines()]
        return {key: float(value) for key, value in data}


def salary_statistics(inc_file):
    data_set = salary_statement_parser(inc_file)
    data_set_values = data_set.values()

    loser_list = '\n'.join([key for key, val in data_set.items() if val < 20000])
    average_salary = sum(data_set_values) / len(data_set_values)

    print(f'оклад менее 20 000 имеют:\n{loser_list}')
    print(f'средний оклад составляет {average_salary:.2f}')


salary_statistics('file_3.txt')
