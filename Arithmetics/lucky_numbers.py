def lucky(n):
    L = list(range(1, int(n) + 1, 2))
    j = 1
    while L[j] <= len(L) - 1:
        L = [L[i] for i in range(len(L)) if (i + 1) % L[j] != 0]
        j += 1
    return(L)


print(lucky(input()))
