from sympy import factorint

n = 1
consecutive_4_factor = 0
while consecutive_4_factor < 4:
    if len(factorint(n)) == 4:
        consecutive_4_factor += 1
    else:
        consecutive_4_factor = 0
    n += 1
print(n - 4)