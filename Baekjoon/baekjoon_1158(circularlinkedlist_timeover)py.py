import sys

answer = 0
n = int(input())
building = []
stack = []
for _ in range(n):
    building.append(int(input()))

for i in range(n):
    while stack and stack[-1] <= building[i]:
        stack.pop()

    answer += len(stack)
    print(answer)
    stack.append(building[i])

print(answer)
