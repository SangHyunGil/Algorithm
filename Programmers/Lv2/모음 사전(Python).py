"""
알파벳의 총 개수는 5개이다.(모음)
총 경우의 수를 살펴보면 다음과 같다.
1 : 5 = 5
2 : 5*5 = 25
3 : 5*5*5 = 125
4 : 5*5*5*5 = 625
5 : 5*5*5*5*5 = 3125

=> 3905 + a 의 복잡도가 나올 것이다.
그러므로 충분히 시간이 될 것이기에 정렬하면 최악에 O(N)만큼이 추가되고
index를 찾는데 최악에 O(N)이 추가된다.
그에 따라, O(N+N+N)이라면 충분히 시간안에 통과가 가능하다.
"""

from itertools import product

def solution(word):
    alpha = "AEIOU"
    words = sorted(set(["".join(w) for i in range(1, 6) for w in product(alpha, repeat=i)]))
    return words.index(word)+1

print(solution("AAAAE"))\

