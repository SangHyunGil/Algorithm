import sys
from itertools import permutations
input = sys.stdin.readline

def solve():
    answer = 0
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = [0] * 100000
    x = int(input())
    for a in arr1:
        arr2[a] = 1

    for a in arr1:
        if x-a < 100000 and arr2[a] and arr2[x-a]:
            answer += 1
    
    print(answer//2)

solve()