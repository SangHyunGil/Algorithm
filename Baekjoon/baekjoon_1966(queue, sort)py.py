import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    answer = []
    paper = list(map(int, input().split()))
    ballon = deque(zip(range(1, n+1), paper))
    
    while len(ballon) > 1:
        b = ballon.popleft()
        answer.append(b[0])
        if b[1] > 0:
            for _ in range(b[1]-1):
                ballon.append(ballon.popleft())

        else:
            for _ in range(abs(b[1])):
                ballon.appendleft(ballon.pop())

    answer.append(ballon[0][0])
    print(*answer)

solve()