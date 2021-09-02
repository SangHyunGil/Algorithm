import sys
from heapq import heappush, heappop
input = sys.stdin.readline

s = input().strip()

PPAP = []
for c in s:
    if len(PPAP) > 2:
        if c == 'P':
            print(PPAP, c)
            if PPAP[-3:] == ['P', 'P', 'A']:
                for _ in range(3): 
                    PPAP.pop()

    PPAP.append(c)

print("PPAP" if PPAP == ['P'] else "NP")