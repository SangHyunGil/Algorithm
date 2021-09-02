import sys
from heapq import heappush, heappop
input = sys.stdin.readline

s = input().strip()
bomb = list(input().strip())
remain = []
for c in s:
    remain.append(c)

    if len(remain) >= len(bomb):
        if remain[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                remain.pop()    

remain = "".join(remain)
print(remain if remain != "" else "FRULA")