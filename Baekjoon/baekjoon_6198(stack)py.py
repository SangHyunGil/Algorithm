import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':  break

    stack = []
    for c in s:
        print(stack, c)
        if c == '(' or c == '[':
            stack.append(c)
        
        elif c == ')':
            if stack[-1] == '(' and stack:
                stack.pop()
            else:
                stack.append(c)

        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

    if stack:
        print("no")
    else:
        print("yes")