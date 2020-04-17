from collections import deque


def binary(number: int) -> str:
    temp = deque()

    while number:
        modulo: int = number % 2
        temp.appendleft(modulo)

        number //= 2

    temp.appendleft('0b')

    return ''.join(map(str, temp))


if __name__ == '__main__':
    text = 'Enter the number to convert: '
    converted = binary(int(input(text)))
    print(f'Your number is: {converted}')
