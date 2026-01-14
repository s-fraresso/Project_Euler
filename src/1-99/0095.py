MAX_TERM = 1_000_000

proper_divisors_sum = [1]*MAX_TERM
for divisor in range(2, MAX_TERM // 2):
    k = 2
    while divisor * k < MAX_TERM:
        proper_divisors_sum[divisor * k] += divisor
        k += 1

seen_terms = set()
smallest_member, max_length = float('+inf'), float('-inf')

for start in range(2, MAX_TERM):
    if start in seen_terms:
        continue

    chain = [start]
    next_term = proper_divisors_sum[start]
    while next_term < MAX_TERM and next_term not in chain and next_term not in seen_terms:
        chain.append(next_term)
        next_term = proper_divisors_sum[next_term]
    
    if next_term >= MAX_TERM or next_term in seen_terms:
        chain_start = len(chain)
    else:
        chain_start = chain.index(next_term)
        if len(chain) - chain_start > max_length:
            max_length = len(chain) - chain_start
            smallest_member = min(chain[chain_start:])
        elif len(chain) - chain_start == max_length:
            smallest_member = min(smallest_member, min(chain[chain_start:]))

    seen_terms.update(chain)


print(smallest_member)