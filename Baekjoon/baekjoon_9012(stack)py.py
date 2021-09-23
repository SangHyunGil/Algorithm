import sys
from collections import deque
input = sys.stdin.readline

def solve():
    card = deque([i for i in range(1, int(input())+1)])
    toggle = 1
    while len(card) > 1:
        if toggle:
            card.popleft()
        else:
            card.append(card.popleft())\

        toggle ^= 1

    print(card.pop())
solve()