from sys import argv


def calc_salary():
    hours = float(argv[1])
    rate_by_hour = float(argv[2])
    reward = float(argv[3])

    salary = hours * rate_by_hour + reward
    print(f'your salary is {salary} dollars' )


calc_salary()
