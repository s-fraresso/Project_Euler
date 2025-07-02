def reciprocal_recurring_cycle_length(d):
    qr_list = [(0, 1)]
    quotient, reste = 0, 1

    while (quotient, reste) not in qr_list[:-1]:
        quotient = reste // d
        reste = (reste % d) * 10
        qr_list.append((quotient, reste))

    cycle_length = 0
    for i in range(len(qr_list) - 2, -1, -1):
        cycle_length += 1
        if qr_list[i] == (quotient, reste):
            break

    return cycle_length


print(max(range(1, 1001), key=lambda d:reciprocal_recurring_cycle_length(d)))