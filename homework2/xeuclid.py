def xeuclid(a,b):
    if b == 0:
        return (1, 0, a)
    else:
        (x, y, d) = xeuclid(b, a % b)
        return (y, x - (a // b) * y, d)

print xeuclid(72,5)