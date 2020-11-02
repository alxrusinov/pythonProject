first_day = int(input('введите результат в первый день '))
target_result = int(input('введите общий ожтдаемый результат '))

target_day = 1
result = first_day

while True:
    print(result)
    if target_result <= result or result >= target_result:
        break

    result = result + result * 0.1
    target_day += 1

print(f'результат будет получен на {target_day} день')
