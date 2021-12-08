import sys
from functools import reduce
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]+[*map(int, input().split())]
for i in range(2, N+1):
    arr[i] += arr[i-1]

for i in range(M):
    i, j = map(int, input().split())
    print(arr[j]-arr[i-1])
