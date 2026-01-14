from sympy import *

n = Symbol('n')

def polynome_interpolateur(lx, ly):
    m = len(ly)
    P = 0
    for i in range(m):
        Q = ly[i]
        for j in range(m):
            if i != j:
                Q *= (n - lx[j]) / (lx[i] - lx[j])
        P += Q
    return P

FIT_sum = 0
U = (1 + n**11) / (1 + n) # polynome générateur de la suite
d = 10 # degré du polynome générateur
lx = [] # abscisses d'interpolation (indices de la suite)
for k in range(1, d + 1):
    lx.append(k)
    OP = polynome_interpolateur(lx, [U.subs(n, x) for x in lx])
    FIT = OP.subs(n, k + 1) # premier terme incorrect si OP est un BOP
    if FIT != U.subs(n, k + 1): # vrai si BOP
        FIT_sum += FIT

print(FIT_sum)