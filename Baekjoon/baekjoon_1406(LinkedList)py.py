import sys
from collections import deque
input = sys.stdin.readline

stack = list(input().rstrip())
queue = deque([])

for _ in range(int(input())):
    command = list(input().rstrip().split())

    if command[0] == 'P':
        stack.append(command[1])
    
    elif command[0] == 'L':
        if stack:
            queue.appendleft(stack.pop())

    elif command[0] == 'D':
        if queue:
            stack.append(queue.popleft())

    else:
        if stack:
            stack.pop()

print("".join(stack)+"".join(queue))