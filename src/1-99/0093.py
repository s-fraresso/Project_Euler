from fractions import Fraction


def consecutive_first_integers(tested_set):
    ordered_set = sorted(tested_set)
    i = 0
    while i < len(ordered_set) - 1 and ordered_set[i] + 1 == ordered_set[i + 1]:
        i += 1
    return i + 1

def compute_reachable_outcomes(digits, memo={}):
    if frozenset(digits) in memo:
        return memo[frozenset(digits)]
    
    if len(digits) == 1:
        return digits
    
    reachable_outcomes = set()
    for operator in ('+', '-', 'x', '/'):
        for op1 in digits:
            for op2 in compute_reachable_outcomes(digits.difference({op1})):
                if operator == '+':
                    reachable_outcomes.add(op1 + op2)
                elif operator == '-':
                    if op1 - op2 > 0:
                        reachable_outcomes.add(op1 - op2)
                    if op2 - op1 > 0:
                        reachable_outcomes.add(op2 - op1)
                elif operator == 'x':
                        reachable_outcomes.add(op1 * op2)
                elif operator == '/':
                    if op2 != 0:
                        reachable_outcomes.add(op1 / op2)
                    if op1 != 0:
                        reachable_outcomes.add(op2 / op1)
    return reachable_outcomes

max_consecutive_targets = float("-inf")
optimal_digits_string = None

for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                reachable_targets = compute_reachable_outcomes({Fraction(a), Fraction(b), Fraction(c), Fraction(d)})
                filtered_targets = map(int, (filter(Fraction.is_integer, reachable_targets)))
                nb_consecutive_targets = consecutive_first_integers(filtered_targets)
                if nb_consecutive_targets > max_consecutive_targets:
                    max_consecutive_targets = nb_consecutive_targets
                    optimal_digits_string = ''.join(map(str, (a, b, c, d)))

print(optimal_digits_string)