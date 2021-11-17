import sys
from itertools import permutations
input = sys.stdin.readline

def count():
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr.count(int(input())))
    # dic = {}
    # for a in arr:
    #     if a in dic:
    #         dic[a] += 1
    #     else:
    #         dic[a] = 1
    # v = int(input())
    # print(dic[v] if v in dic else 0)

count()