LINES = ((0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1))
EXTERNAL_NODES = (0, 3, 5, 7, 9)


def ring_digit_string(ring):
    first_node_index = min(range(5), key=lambda i: ring[EXTERNAL_NODES[i]])
    digit_string = ""
    for i in range(5):
        for j in LINES[(first_node_index + i) % 5]:
            digit_string += str(ring[j])
    return digit_string


def is_ring_valid(ring, target_sum):
    for line in LINES:
        if all(map(lambda i:ring[i] is not None, line)) and sum(ring[i] for i in line) != target_sum:
            return False
    return True


def build_magic_ring(current_ring, available_numbers, target_sum):
    if len(available_numbers) == 0:
        return {tuple(current_ring)}
    
    valid_rings = set()

    for next_number in available_numbers:
        new_ring = current_ring.copy()
        new_ring[len(current_ring) - len(available_numbers)] = next_number
        if is_ring_valid(new_ring, target_sum):
            valid_rings.update(build_magic_ring(new_ring, available_numbers.difference({next_number}), target_sum))

    return valid_rings


maximum_string = float('-inf')
for target_sum in range(13, 28):
    for ring in build_magic_ring([10] + [None]*9, set(range(1, 10)), target_sum): # 10 must be on external node for 16-digit string
        maximum_string = max(maximum_string, int(ring_digit_string(ring)))
print(maximum_string)