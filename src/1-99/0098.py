from math import ceil

def find_largest_anagramic_square(input_file):
    counterized_words = [(word, counterize_word(word)) for word in read_word_list(input_file)]
    anagram_groups = group_anagrams(counterized_words)
    max_nb_digit = max(sum(counter) for counter in anagram_groups)
    square_anagrams = generate_square_anagrams(max_nb_digit)
    max_square = -1
    for counter in sorted(anagram_groups.keys(), key=lambda ckey:sum(ckey), reverse=True):
        if max_square > 10**(sum(counter)):
            continue
        print(anagram_groups[counter])
        for sqcounter in square_anagrams:
            if reduced_counter(sqcounter) != reduced_counter(counter):
                continue
            print("\t", square_anagrams[sqcounter])
            for i in range(len(anagram_groups[counter])):
                word = anagram_groups[counter][i]
                for j in range(len(square_anagrams[sqcounter]) - 1, -1, -1):
                    sq = square_anagrams[sqcounter][j]
                    wordified_square = list(str(sq))
                    is_valid = True
                    for a in range(len(wordified_square)):
                        for b in range(len(wordified_square)):
                            if word[a] == word[b] and wordified_square[a] != wordified_square[b]:
                                is_valid = False
                                break
                        if not is_valid:
                            break
                    if not is_valid:
                        continue
                    for k in range(i + 1, len(anagram_groups[counter])):
                        base_word = list(word)
                        target_word = list(anagram_groups[counter][k])
                        for arr in compute_rearrangements(base_word, target_word, 0):
                            new_sq = int(''.join([wordified_square[arr.index(i)] for i in range(len(arr))]))
                            for c in range(len(square_anagrams[sqcounter])):
                                if c != j and square_anagrams[sqcounter][c] == new_sq:
                                    print(anagram_groups[counter], sq, new_sq, arr)
                                    max_square = max(max_square, sq, new_sq)
    return max_square


def compute_rearrangements(base_word, target_word, i):
    if i >= len(target_word):
        return [[]]
    c = base_word[i]
    arrangements = []
    for j in (k for k in range(len(target_word)) if target_word[k] == c):
        new_target = target_word[:]
        new_target[j] = '0'
        for arr in compute_rearrangements(base_word, new_target, i + 1):
            arrangements.append([j] + arr)
    return arrangements


def reduced_counter(counter):
    rcount = [0]*26
    i = 0
    for n in counter:
        if n == 0:
            continue
        j = i
        while j > 0 and rcount[j - 1] < n:
            rcount[j], rcount[j - 1] = rcount[j -1], rcount[j]
            j -= 1
        rcount[j] = n
        i += 1
    return rcount


def generate_square_anagrams(max_nb_digit):
    square_anagrams = dict()
    for n in range(ceil(10**(max_nb_digit / 2))):
        square = n * n
        counter = counterize_integer(square)
        if counter in square_anagrams:
            square_anagrams[counter].append(square)
        else:
            square_anagrams[counter] = [square]
    return dict(filter(lambda item: len(item[1]) > 1, square_anagrams.items()))


def counterize_integer(integer):
    counter = [0]*10 # counter[i] est le nombre de fois que i apparaît dans l'écriture décimale de integer
    for digit in str(integer):
        counter[int(digit)] += 1
    return tuple(counter)


def group_anagrams(counterized_words):
    anagrams = dict()
    for cword in counterized_words:
        word, counter = cword
        if counter in anagrams:
            anagrams[counter].append(word)
        else:
            anagrams[counter] = [word]
    return dict(filter(lambda item: len(item[1]) > 1, anagrams.items()))


def read_word_list(input_file):
    with open(input_file, 'r') as f:
        words = [word[1:-1] for word in f.readline().split(",")]
    return words


def counterize_word(word):
    counter = [0]*26 # counter[i] est le nombre de fois que la i-ème lettre de l'alphabet apparaît dans word
    for letter in word:
        counter[ord(letter) - ord('A')] += 1
    return tuple(counter)


print(find_largest_anagramic_square("input_files\\0098_words.txt"))