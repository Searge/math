def dozen(x):
    """ Показати усі множники 12-ти
    """
    n = 0
    for i in range(x + 1):
        n += 12
        print(12, '×', i, '=', n)


dozen(int(input('Наскільки помножити 12: ')))
