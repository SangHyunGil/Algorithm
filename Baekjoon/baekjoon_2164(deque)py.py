import sys
input = sys.stdin.readline

def solve():
    answer = [[], 0]
    stack = []
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    
    k = 0
    for i in range(1, n+1):
        answer[0].append('+')
        stack.append(i)
        print(answer)
        while stack and k < n and stack[-1] == arr[k]:
            stack.pop()
            answer[0].append('-')
            answer[1] += 1
            k += 1

    if answer[1] == n:
        for ans in answer[0]:
            print(ans)
    else:
        print("NO")

solve()