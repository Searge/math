def karatsuba(x, y):
    n = len(str(x))
    rank = 10 ** n
    n05 = int(n * .5)
    rank05 = 10 ** n05
    a, b = x // rank05, x % rank05
    c, d = y // rank05, y % rank05
    ac, bd = a * c, b * d
    r = rank * ac + rank05 * ((a + b) * (c + d) - ac - bd) + bd
    return r


if __name__ == "__main__":
    x, y = [int(input(_)) for _ in range(2)]
    print(karatsuba(x, y))
