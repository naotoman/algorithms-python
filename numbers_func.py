def prime_fact_dic(n):
    """Returns the dictionary that contains the prime factors of integer `n`.

    Args:
      n (int): An integer greater than 1.
    
    Returns:
      dict: The dictionary whose keys are the prime factors of `n` and values are the number of those appearances.
    """
    facts = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            facts[d] = facts.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        facts[n] = 1
    return facts


def prime_fact_list(n):
    """Returns the list that contians the prime factors of integer `n`.

    Args:
      n (int): An integer greater than 1.
    
    Returns:
      list: The list that contains the all prime factors of `n`.
    """
    facts = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            facts.append(d)
            n //= d
        d += 1
    if n > 1:
        facts.append(n)
    return facts