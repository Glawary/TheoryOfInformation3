import sys

amount_mes_string = input('Введите количество элементарных сообщений: ')
try:
    amount_mes = int(amount_mes_string)
    p = []
    l = []
    n_m = 0
    for i in range(amount_mes):
        p_string = input('\nВведите вероятность появления {0} сообщения: '.format(i + 1))

        try:
            p.append(float(p_string))
        except ValueError:
            print(
                'Проверьте правильность ввода! Вероятность появления сообщения должна представлять из себя дробное или целое положительное число, не превышающее 1.')
            sys.exit()
        if p[i] < 0 or p[i] > 1:
            print(
                'Проверьте правильность ввода! Вероятность появления сообщения должна представлять из себя дробное или целое положительное число, не превышающее 1.')
            sys.exit()

        l_string = input('Введите длину кодовой комбинации для {0} сообщения: '.format(i + 1))

        try:
            l.append(int(l_string))
        except ValueError:
            print(
                'Проверьте правильность ввода! Длина кодовой комбинации должна представлять из себя целое положительное число.')
        if l[i] < 0:
            print(
                'Проверьте правильность ввода! Длина кодовой комбинации должна представлять из себя целое положительное число.')
            sys.exit()

        n_m += l[i] * p[i]
    print('\nСредняя длина кодовой комбинации при передаче сообщения: {0}'.format(round(n_m, 1)))

except ValueError:
    print('Проверьте правильность ввода! Количество элементарных сообщений должно представлять из себя целое число.')

input('\nНажмите ENTER для выхода из программы')