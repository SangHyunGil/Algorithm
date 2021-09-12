import sys
from collections import deque
input = sys.stdin.readline



for _ in range(int(input())):
    stack = []
    queue = deque([])

    for command in input().rstrip():
        if command == '<':
            if stack:
                queue.appendleft(stack.pop())

        elif command == '>':
            if queue:
                stack.append(queue.popleft())

        elif command == '-':
            if stack:
                stack.pop()

        else:
            stack.append(command)

    

    print("".join(stack)+"".join(queue))