def factorial2(n):
    x = 1
    for i in range(x, n + x):
        x *= i
    return x


if __name__ == '__main__':
    print(factorial2(int(input('Write your number: '))))
