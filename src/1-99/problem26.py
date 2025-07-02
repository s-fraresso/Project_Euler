def reciprocal_recurring_cycle_length(d):
    remainder_list = [1]
    remainder = 1

    while remainder not in remainder_list[:-1]:
        remainder = (remainder % d) * 10
        remainder_list.append(remainder)

    cycle_length = 0
    for i in range(len(remainder_list) - 2, -1, -1):
        cycle_length += 1
        if remainder_list[i] == remainder:
            break

    return cycle_length


print(max(range(1, 1001), key=lambda d:reciprocal_recurring_cycle_length(d)))