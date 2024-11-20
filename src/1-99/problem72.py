from sympy.functions.combinatorial.numbers import totient

def count_reduced_proper_fractions(limit):
        return sum(totient(i) for i in range(2, limit + 1))

print(count_reduced_proper_fractions(1_000_000)) # 303963552391
