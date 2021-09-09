import sys
input = sys.stdin.readline

answer = ""
stack = []
priority = {'/' : 2, '*' : 2, '+' : 1, '-' : 1, '(' : 0}
s = input().strip()
for c in s:
    if c == '(':
        stack.append(c)

    elif c == ')':
        while stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

    elif 'A' <= c <= 'Z':
        answer += c

    else:
        while stack and priority[stack[-1]] >= priority[c]:
            answer += stack.pop()
        stack.append(c)

while stack: answer += stack.pop()
print(answer)