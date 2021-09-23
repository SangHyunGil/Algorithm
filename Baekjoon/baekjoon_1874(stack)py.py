import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    stack = []
    expression = input().strip()
    value = {chr(ord('A')+i) : int(input()) for i in range(n)}

    for ex in expression:
        if ex == '*' or ex == '+' or ex == '-' or ex =='/':
            b = stack.pop()
            a = stack.pop()

            stack.append(eval(str(a)+ex+str(b)))
        else:
            stack.append(value[ex])


    print("%.2f"%float(stack[0]))

solve()