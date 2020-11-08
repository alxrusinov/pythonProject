def get_user_data(**kwargs):
    parameters = {'first_name': 'вы не ввели имя', 'last_name': 'вы не ввели фамилию',
                  'birth': 'вы не ввели год рождения', 'place': 'вы не ввели место рождения',
                  'email': 'вы не ввели email', 'phone': 'вы не ввели телефон'}
    data_is_wrong = False
    result = ''

    for parameter in parameters.keys():
        if parameter not in kwargs:
            data_is_wrong = True
            result = ''
            print(f'данные не полные: {parameters[parameter]}')
        if not data_is_wrong:
            result = result + f'{kwargs[parameter]} '

    if not data_is_wrong:
        print(result.rstrip())
    else:
        print('упс! данные введены неполностью :(')


get_user_data(first_name='pennywise', last_name='clown', place='Москва', birth='1923', email='evil@clown.ru',
              phone='8800888000')
