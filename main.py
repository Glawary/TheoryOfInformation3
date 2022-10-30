import sys

count_mes_string = input('Введите количество элементарных сообщений: ')
try:
    count_mes = int(count_mes_string)
    posibility = []
    length = []
    mean = 0
    for i in range(count_mes):
        posibility_string = input('\nВведите вероятность появления {0} сообщения: '.format(i + 1))

        try:
            posibility.append(float(posibility_string))
        except ValueError:
            print(
                'Проверьте правильность ввода! Вероятность появления сообщения должна представлять из себя дробное или целое положительное число, не превышающее 1.')
            sys.exit()
        if posibility[i] < 0 or posibility[i] > 1:
            print(
                'Проверьте правильность ввода! Вероятность появления сообщения должна представлять из себя дробное или целое положительное число, не превышающее 1.')
            sys.exit()

        length_string = input('Введите длину кодовой комбинации для {0} сообщения: '.format(i + 1))

        try:
            length.append(int(length_string))
        except ValueError:
            print(
                'Проверьте правильность ввода! Длина кодовой комбинации должна представлять из себя целое положительное число.')
        if length[i] < 0:
            print(
                'Проверьте правильность ввода! Длина кодовой комбинации должна представлять из себя целое положительное число.')
            sys.exit()

        mean += length[i] * posibility[i]
    print('\nСредняя длина кодовой комбинации при передаче сообщения: {0}'.format(round(mean, 1)))

except ValueError:
    print('Проверьте правильность ввода! Количество элементарных сообщений должно представлять из себя целое число.')

input('\nНажмите ENTER для выхода из программы')