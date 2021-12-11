import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
DP = [0] * 1000001
DP[0] = 0; DP[1] = 1


for i in range(2, 1000001):
    DP[i] = (DP[i-1]+DP[i-2])%1000000000

if N == 0:
    print(0)
    print(0)

elif N > 0:
    print(1)
    print(DP[N])
else:
    print(1 if abs(N) % 2 else -1)
    print(DP[abs(N)])