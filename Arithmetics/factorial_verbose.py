def factorial(n):
    x = 1
    for i in range(x, n + x):
        x *= i
    return x


def factorial_numbers(number):
    for i in range(number):
        yield f'{i + 1} × '


def factorial_verbose(n):
    result = ''.join([x for x in factorial_numbers(n)])
    result = ' '.join([result[:len(result) - 3], '=', str(factorial(n))])
    return result


if __name__ == '__main__':
    print(factorial_verbose(int(input('Write your number: '))))
