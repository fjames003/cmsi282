from modpow import modpow
import math

def mod_double_pow(a, b, c, p):
	if is_prime(p):
	    b_c = modpow(b, c, p - 1)
	    return modpow(a, b_c, p)
	else:
		raise ValueError("The value 'p' was not prime")

def is_prime(n):
	return all(n % i for i in xrange(2, int(math.ceil(math.sqrt(n)))))

