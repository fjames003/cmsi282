def modpow(x, y, n):
    if y == 0:
        return 1
    else:
        z = modpow(x, y // 2, n)
        if y % 2 == 0:
            return (z ** 2) % n
        else:
            return (x * (z ** 2)) % n

