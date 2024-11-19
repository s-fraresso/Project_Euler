def somme_fibo_pair(threshold):
    total = 0
    prev, current = 1, 1
    nxt = 2
    while nxt < threshold:
        prev = current
        current = nxt
        nxt = current + prev

        if current % 2 == 0:
            total += current
    return total

print(somme_fibo_pair(4_000_000))