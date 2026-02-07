from sympy import primerange
from fractions import Fraction

N = 10**8

class Digit_Node:
    def __init__(self):
        self.nb_primes = 0
        self.children_nodes = [None, None]

    def add_child(self, digit):
        self.children_nodes[digit] = Digit_Node()
        return self.children_nodes[digit]


def add_prime_to_tree(p, tree):
    current_node = tree
    current_node.nb_primes += 1
    for digit in map(int, bin(p)[:1:-1]):
        if current_node.children_nodes[digit] is None:
            current_node = current_node.add_child(digit)
        else:
            current_node = current_node.children_nodes[digit]
        current_node.nb_primes += 1


def expected_points(node):
    if node.children_nodes[0] is None and node.children_nodes[1] is None:
        return 0
    
    if node.children_nodes[0] is None or node.children_nodes[1] is None:
        next_node = node.children_nodes[0] if node.children_nodes[1] is None else node.children_nodes[1]
        prob_continue = Fraction(next_node.nb_primes, node.nb_primes) 
        return prob_continue * (1 + expected_points(next_node))

    prob_zero = Fraction(node.children_nodes[0].nb_primes, node.nb_primes)
    prob_one = Fraction(node.children_nodes[1].nb_primes, node.nb_primes)
    return (max(prob_one, prob_zero) +
            prob_zero * expected_points(node.children_nodes[0]) +
            prob_one * expected_points(node.children_nodes[1]))


prime_tree = Digit_Node()
for p in primerange(N + 1):
    add_prime_to_tree(p, prime_tree)
print(round(float(expected_points(prime_tree)), 8))