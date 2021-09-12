import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
stack = []

idx = 0
while arr:
    if idx <= len(arr)-K:
        idx += K-1
    else:
        idx = (idx+K-1) % len(arr)

    stack.append(arr.pop(idx))
    print(stack, arr, idx)
answer = '<'
for s in stack:
    answer += str(s) + ", "

for a in arr:
    answer += str(a) + ", "
answer = answer[:-2]+">"

print(answer)