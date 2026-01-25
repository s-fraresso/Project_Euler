chains = {(1,)}
min_mul = {1:0, 191:11}

def min_multiplications(target):
	global chains, min_mul
	while not target in min_mul:
		new_chains = set()
		for chain_start in chains:
			for term in chain_start:
				if chain_start[-1] + term <= 200:
					new_chains.add(chain_start + (chain_start[-1] + term,))
				else:
					new_chains.add(chain_start)
		chains = new_chains
		for chain in chains:
			if chain[-1] not in min_mul:
				min_mul[chain[-1]] = len(chain) - 1
	return min_mul[target]


total = 0
for k in range(1, 201):
  print(k)
  total += min_multiplications(k)
print(total)