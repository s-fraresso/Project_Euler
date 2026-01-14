def rotate(n, nb_rotation):
    l = [int(digit) for digit in str(n)]
    for _ in range(nb_rotation):
        l.append(l.pop(0))
    return sum(l[-(i+1)] * 10**i for i in range(len(l)))

def is_circular(p, sieve):
    for i in range(1, len(str(p))):
        if not sieve[rotate(p, i)]:
            return False
    return True

def count_circular_primes(limit):
    sieve = dict()
    for n in range(2, limit):
        if n not in sieve:
            sieve[n] = True
            for multiple in range(2*n, limit, n):
                sieve[multiple] = False
    
    nb_circulars = 0
    for p in filter(lambda x: sieve[x], sieve):
        if is_circular(p, sieve):
            nb_circulars += 1
    
    return nb_circulars

print(count_circular_primes(1_000_000)) # 55