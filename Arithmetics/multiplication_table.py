n = int(input('Write multiplier: ')) + 1

for i in range(1, n):
    print(*range(i, i * n, i), sep='\t')

print('\n')

for a in range(2, n):
    for b in range(2, n):
        print('{} × {} = {}'.format(b, a, a * b), end='\t')
    print()
