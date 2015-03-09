def lcm(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a * b // gcd(a,b)
        
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
