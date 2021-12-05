import sys
input = sys.stdin.readline

ans = 0
N, M = map(int, input().split())

def find(num):
    global ans

    if N <= num <= M:
        ans += 1

    elif num > M:
        return
    
    find(num * 10 + 4)
    find(num * 10 + 7)

find(0)
print(ans)