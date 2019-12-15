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

# #二項係数(mod)
def comb(n, k, mod, fac, finv):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

# 階乗の逆元(mod)
def factorials_inv_mod(n, mod):
    inv = [1] * (n + 1)
    factorials_inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        factorials_inv[i] = factorials_inv[i - 1] * inv[i] % mod
    return factorials_inv

# 階乗(mod)
def factorials_mod(n, mod):
    factorials = [1] * (n + 1)
    for i in range(2, n+1):
        factorials[i] = (factorials[i-1] * i) % mod
    return factorials

# 二分累乗法(mod) #べき乗 #冪乗
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