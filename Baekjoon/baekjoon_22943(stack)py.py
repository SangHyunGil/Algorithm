import sys
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        stack = []
        s = input().rstrip()

        for c in s:
            if stack:
                if c == "(":
                    stack.append(c)

                else:
                    if stack[-1] == "(":
                        stack.pop()            
                
            else:
                stack.append(c)

        if stack:
            print("NO")
        else:
            print("YES")
solve()