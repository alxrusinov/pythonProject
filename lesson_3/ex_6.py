def int_func(word):
    word_is_valid = True
    for i in word:
        if 97 > ord(i) or ord(i) > 122:
            word_is_valid = False
            break
    return word.capitalize() if word_is_valid else None


def capitalize_it(string):
    word_list = string.split()
    result = []
    for i in range(len(word_list)):
        new_word = int_func(word_list[i])
        if new_word:
            result.append(new_word)

    return ' '.join(result)


print(capitalize_it('clown foo 45 роза'))
