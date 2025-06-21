def distinct_powers(limit):
    generated = []
    total = 0
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            power = a**b
            if power not in generated:
                generated.append(power)
                total += 1
    return total

print(distinct_powers(100)) # 9183