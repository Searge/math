N = int(input())
Suma = sum([int(x) for x in str(N)])
last_int = int(str(N)[-1:])
last2_int = int(str(N)[-2:])

print('Сумма усіх цифр', '\t', Suma)
print("Дві ост. цифри", "\t", last2_int)

if last2_int == 00:
    print("Дві ост. цифри — нулі", "\t", 'Так')
elif (last_int % 2) == 0:
    print("Остання цифра ділиться на 2", "\t", 'Так')
elif (last2_int % 4) == 0:
    print("Дві ост. цифри ділиться на 4", "\t", 'Так')
elif last2_int == 5:
    print("Остання цифра — 5", "\t", 'Так')

print("Дві ост. цифри 25; 50; 75", "\t", N % 2)

print("Сума його цифр ділиться на 3", "\t", N % 2)
print("Сума цифр ділиться на 9", "\t", N % 2)
