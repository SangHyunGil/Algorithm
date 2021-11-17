import sys
from collections import deque
input = sys.stdin.readline
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = input().rstrip()
B = input().rstrip()

queue = deque([])
for a, b in zip(A, B):
    queue.append(alpha[ord(a)-ord('A')])
    queue.append(alpha[ord(b)-ord('A')])

while len(queue) != 2:
    for i in range(len(queue)-1):
        queue.append((queue.popleft()+queue[0]) % 10)
    queue.popleft()

print("".join(map(str,queue)))

