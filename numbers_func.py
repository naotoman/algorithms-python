# 素因数分解
def prime_fact_dic(n):
    """Returns the dictionary that contains the prime factors of integer `n`.
    Args:
      n (int): An integer greater than 1.
    Returns:
      dict: The dictionary whose keys are the prime factors of `n` and values are the number of those appearances.
    """
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors

# 素因数分解
def prime_fact_list(n):
    """Returns the list that contians the prime factors of integer `n`.
    Args:
      n (int): An integer greater than 1.
    Returns:
      list: The list that contains the all prime factors of `n`.
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# 繰り返し自乗法(mod) #べき乗 #冪乗
def pow_mod(base, exp, mod):
    res = 1
    x = base
    while exp > 0:
        if exp & 1:
            res = (res * x) % mod
        x = (x ** 2) % mod
        exp >>= 1
    return res

# 最大公約数 #ユークリットの互除法
def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while a > 0:
        a, b = b % a, a
    return b

# 階乗
class Factorials(object):
    def __init__(self, n, mod):
        inv = [1] * (n + 1)
        self.__mod = mod
        self.__fac = [1] * (n + 1)
        self.__fac_inv = [1] * (n + 1)
        for i in range(2, n+1):
            self.__fac[i] = (self.__fac[i-1] * i) % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            self.__fac_inv[i] = self.__fac_inv[i - 1] * inv[i] % mod
        
    def fac(self, n):
            return self.__fac[n]

    def perm(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        return self.__fac[n] * self.__fac_inv[n - k] % self.__mod

    def comb(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        return self.__fac[n] * (self.__fac_inv[k] * self.__fac_inv[n - k] % self.__mod) % self.__mod