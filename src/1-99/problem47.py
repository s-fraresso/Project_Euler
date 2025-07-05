from sympy import factorint

n = 1
while any(len(factorint(n + i).keys()) < 4 for i in range(4)):
    n += 1
print(n)