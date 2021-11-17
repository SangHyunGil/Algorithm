import sys
from itertools import permutations
input = sys.stdin.readline

def getRoom(n, k):
    if n == 0: return 0
    elif n < k: return 1
    else: return n//k+1 if abs(n/k)-n//k > 0 else n//k

def solve():
    answer = 0
    N, K = map(int, input().split())
    room = [[0, 0] for _ in range(7)]

    for _ in range(N):
        S, Y = map(int, input().split())
        room[Y][S] += 1

    for i in range(1, 7):
        answer += getRoom(room[i][0], K) + getRoom(room[i][1], K)

    print(answer)

solve()