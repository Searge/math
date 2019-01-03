
N = int(input())

divider = dict((i, i) for i in range(2, 20 + 1))


list_int = [int(x) for x in str(N)]
last_int = int(str(N)[-1:])
last2_int = int(str(N)[-2:])
Suma = sum(list_int)


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

logic = ((int(str(N)[:-1]) * 3 + int(str(N)[-1:])) % 7) \
    and ((int(str(N)[:-2]) * 2 + int(str(N)[-2:])) % 7) \
    and ((int(str(N)[:-1]) + 5 * int(str(N)[-1:])) % 7)

if logic == 0:
    print("Число ділиться на 7", "\t", 'Так')


def find_divider(N):
    even(N)
    odd(N)
    div5(N)


find_divider(N)
