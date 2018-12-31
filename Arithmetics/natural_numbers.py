N = int(input())
list_int = [int(x) for x in str(N)]
last_int = int(str(N)[-1:])
last2_int = int(str(N)[-2:])
Suma = sum(list_int)

print(list_int)
print('Сумма усіх цифр', '\t', '+'.join(str(list_int)), '=', Suma)
print("Дві ост. цифри", "\t", last2_int)


def even(N):
    if last2_int == 00:
        print("Дві ост. цифри — нулі", "\t", 'Так')
    elif (last_int % 2) == 0:
        print("Остання цифра ділиться на 2", "\t", 'Так')
    if (last2_int % 4) == 0:
        print("Дві ост. цифри ділиться на 4", "\t", 'Так')


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


def find_divider(N):
    even(N)
    odd(N)
    div5(N)


find_divider(N)
