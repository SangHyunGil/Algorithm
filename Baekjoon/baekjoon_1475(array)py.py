import sys
from itertools import permutations
input = sys.stdin.readline

def solve():
    alpha = [0] * 26
    for a in input().rstrip():
        alpha[ord(a)-ord('a')] += 1
    
    for a in input().rstrip():
        alpha[ord(a)-ord('a')] -= 1

    print(sum(map(abs, alpha)))

solve()