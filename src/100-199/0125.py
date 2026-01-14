SQUARES = [n**2 for n in range(7072)] # 7071² + 7072² > 10^8
seen_palindromes = set()
palindromic_sum = 0

for nb_squares in range(2, len(SQUARES)):
    square_sum = sum(SQUARES[:nb_squares])

    for i in range(nb_squares, len(SQUARES)):
        square_sum -= SQUARES[i - nb_squares]
        square_sum += SQUARES[i]

        if square_sum >= 10**8:
            break

        if str(square_sum) == str(square_sum)[::-1] and square_sum not in seen_palindromes:
            seen_palindromes.add(square_sum)
            palindromic_sum += square_sum

print(palindromic_sum)