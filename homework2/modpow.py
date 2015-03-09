def modpow(x, y, n):
    if y == 0:
        return 1
    else:
        z = modpow(x, y // 2, n)
        if y % 2 == 0:
            return (z ** 2) % n
        else:
            return (x * (z ** 2)) % n

print modpow(2*123456789, 3*987654321, 987654321), "\n" + str(modpow(2*123456789, 3*987654321, 100))
