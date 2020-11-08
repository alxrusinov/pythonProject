words = input('введите несколько слов, разделенных пробелами ')

word_list = words.split()

for index in range(len(word_list)):
    print(f'{index + 1}. {word_list[index][:11]}')
