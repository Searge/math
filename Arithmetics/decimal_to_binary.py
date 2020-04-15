from collections import deque


def binary(n: int) -> str:
    temp = deque()

    while n > 0:
        if n % 2 == 1:
            temp.appendleft('1')
        else:
            temp.appendleft('0')
        n //= 2

    temp.appendleft('0b')

    return ''.join(temp)


if __name__ == '__main__':
    text = 'Enter the number to convert: '
    converted = binary(int(input(text)))
    print(f'Your number is: {converted}')
