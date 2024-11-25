from itertools import permutations

def list_to_int(l):
    n = 0
    for i in range(len(l)):
        n += l[-(i + 1)] * 10**i
    return n

def sum_pandigital_product():
    pandigital_products = []
    for perm in permutations(i for i in range(1, 10)):
        product = list_to_int(perm[5:])
        for mult_i in range(1, 4):
            multiplicand = list_to_int(perm[:mult_i])
            multiplier = list_to_int(perm[mult_i:5])
            if multiplicand * multiplier == product and product not in pandigital_products:
                print(multiplicand, multiplier, product)
                pandigital_products.append(product)
    s = 0
    for product in pandigital_products:
        s += product
    return s
    

print(sum_pandigital_product()) # 45228
