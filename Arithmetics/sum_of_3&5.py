# Multiples of 3 and 5
# https://projecteuler.net/problem=1
def find_suma(x):
    suma = []
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            suma.append(i)
    print(suma)
    print(sum(suma))


find_suma(1000)
