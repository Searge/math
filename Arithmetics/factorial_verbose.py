import factorial


def factorial_verbose(number):
    for i in range(number):
        yield f'{i + 1} x '


n = int(input('Write your number: '))

result = ''.join([x for x in factorial_verbose(n)])
result = ' '.join([result[:len(result) - 3],
                   '=', str(factorial(n))])

print(result)
