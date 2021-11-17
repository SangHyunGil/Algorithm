import sys
from itertools import permutations
input = sys.stdin.readline

def solve():
    answer = []
    for _ in range(int(input())):
        alpha = [0] * 26
        A, B = map(list, input().strip().split())
        A.sort()
        B.sort()
        if A == B:
            print("Possible")
        else:
            print("Impossible")

solve()