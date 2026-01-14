from sympy import sqrt, Eq, simplify
from math import copysign


def sign(x):
    return copysign(1, x)


def read_triangles(input_file):
    triangles = []
    with open(input_file, 'r') as f:
        for line in f:
            line = tuple(map(int, line.split(',')))
            triangles.append([(line[2 * i], line[2 * i + 1]) for i in range(3)])
    return triangles


def segment_length(P, Q):
    x1, y1 = P
    x2, y2 = Q
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# d'après https://fr.wikipedia.org/wiki/Formule_de_H%C3%A9ron#Pour_une_mise_en_%C5%93uvre_num%C3%A9rique
def triangle_area(P, Q, R):
    length1, length2, length3 = segment_length(P, Q), segment_length(Q, R), segment_length(R, P)
    a = max(length1, length2, length3)
    c = min(length1, length2, length3)
    b = length1 + length2 + length3 - a - c
    return 1/4 * sqrt((a + b + c) * (c - (a - b)) * (c + (a - b)) * (a + (b - c)))


def contains_point(triangle, S):
    P, Q, R = triangle
    if sign(P[0]) == sign(Q[0]) == sign(R[0]) or sign(P[1]) == sign(Q[1]) == sign(R[1]):
        return False
    return bool(simplify(Eq(triangle_area(P, Q, R), (triangle_area(P, Q, S) + triangle_area(P, S, R) + triangle_area(S, Q, R)))))


print(sum(contains_point(triangle, (0, 0)) for triangle in read_triangles("input_files\\0102_triangles.txt")))