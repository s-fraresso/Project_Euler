from itertools import permutations
from collections import Counter

# De la pure chance, aucune justification que chaque chiffre est différent


for perm in permutations(range(10), 5):
    number = int('1' + "".join(map(str, perm)))
    digits = Counter(str(number))
    if all(digits == Counter(str(number * i)) for i in range(2, 7)):
        print(number)
        break