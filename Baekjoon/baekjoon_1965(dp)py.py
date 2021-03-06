import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int, input().split())
    ans = 0 if N != 0 else 1
    for i in range(N, M+1):
        while i > 1:
            if not i % 10:
                ans += 1
            i //= 10
    print(ans)
