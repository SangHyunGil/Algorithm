import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    ans = 0
    N, M = map(int, input().split())
    for i in range(N, M+1):
        ans += str(i).count('0')
    print(ans)