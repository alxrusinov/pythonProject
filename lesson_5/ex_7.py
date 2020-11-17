import json


def read_data_from_file(source_file):
    with open(source_file, 'r', encoding='utf-8') as source:
        return source.readlines()


def write_to_json(data, target_file):
    with open(target_file, 'w', encoding='utf-8') as target:
        json.dump(data, target)


def get_company_info(data_source):
    companies = {}
    average_profit = {'average_profit': 0}

    for company in data_source:
        company_name, form, revenue, cost = company.split()
        profit = float(revenue) - float(cost)
        average_profit['average_profit'] = average_profit['average_profit'] + profit if profit > 0 else average_profit[
            'average_profit']
        companies[company_name] = profit
    else:
        return [companies, average_profit]


def main_function(source_file, target_file):
    result = get_company_info(read_data_from_file(source_file))
    write_to_json(result, target_file)


main_function('file_7.txt', 'file_7.json')
