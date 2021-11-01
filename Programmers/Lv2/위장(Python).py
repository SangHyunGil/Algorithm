from itertools import product

def solution(word):
    alpha = "AEIOU"
    words = sorted(set(["".join(w) for i in range(1, 6) for w in product(alpha, repeat=i)]))
    return words.index(word)+1

print(solution("AAAAE"))