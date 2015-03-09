# Output: (x, y, d) -> where d = gcd, y = inverse
# Input: euclid(127, 2)
# Returns: (1, -63, 1)


def euclid(a,b):
    if b == 0:
        return (1, 0, a)
    else:
        (x, y, d) = euclid(b, a % b)
        return (y, x - (a // b) * y, d)