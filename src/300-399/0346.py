total = 1 # 1 is a strong repunit

repunits = set()

for b in range(2, 1_000_000 + 1):
    for n in range(3, 40): # log_2(10^12) ~= 39
        repunit = (b**n - 1) // (b - 1)
        if repunit > 1_000_000_000_000:
            break
        if repunit in repunits:
            continue
        repunits.add(repunit)
        total += repunit

print(total)