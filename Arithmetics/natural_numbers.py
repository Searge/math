
N = int(input())

divider = dict((i, i) for i in range(2, 20 + 1))
large_div = (22, 25, 26, 27, 32, 33, 37, 49)

list_int = [int(x) for x in str(N)]
Suma = sum(list_int)

last_int = int(str(N)[-1:])
last2_int = int(str(N)[-2:])

if len(list_int) > 2:
    first_minus_last = (int(str(N)[:-1]))
    first_minus_2_last = (int(str(N)[:-2]))
    logic = ((first_minus_last * 3 + last_int) % 7)\
        and (((first_minus_2_last * 2 + last2_int)) % 7)\
        and ((first_minus_last + 5 * last_int) % 7)


print('Сумма усіх цифр', '\t', ' + '.join(str(x) for x in list_int), '=', Suma)
print("Дві ост. цифри", "\t", last2_int)


def even(N):
    if last2_int == 00:
        print("Дві ост. цифри — нулі", "\t", 'Так')
    elif (last_int % divider[2]) == 0:
        print(f"Остання цифра ділиться на {divider[2]} \t")
    if (last2_int % divider[4]) == 0:
        print(f"Дві ост. цифри ділиться на {divider[4]}")


def odd(N):
    if Suma % 9 == 0:
        print("Сума цифр ділиться на 9", "\t", 'Так')
    elif Suma % 3 == 0:
        print("Сума його цифр ділиться на 3", "\t", 'Так')


def div5(N):
    if last2_int == 5:
        print("Остання цифра — 5", "\t", 'Так')
    elif last2_int == (25 or 50 or 75):
        print("Дві ост. цифри 25; 50; 75", "\t", 'Так')


if N % divider[2] == N % 3:
    print("Число ділиться на 6", "\t", 'Так')


if N == 7:
    print(f"Число {N} ÷ {divider[7]} \t = {N / divider[7]}")
elif logic == 0:
    print(f"Число {N} ÷ {divider[7]} \t = {N / divider[7]}")


def find_divider(N):
    even(N)
    odd(N)
    div5(N)


find_divider(N)
