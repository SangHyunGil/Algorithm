import sys,time
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def isValid(i):
    if 0 <= i < n:
        return True
    else:
        return False

def solve(x):
    if visited[x]:
        return

    for i in range(1, jump+1):
        nx = x+i
        if isValid(nx) and not visited[nx]:
            visited[nx] = 1
            solve(nx)

        nx = x-i
        if isValid(nx) and not visited[nx]:
            visited[nx] = 1
            solve(nx)

n = int(input())
visited = [1] + [0] * (n-1)
rock = [*map(int, input().split())]
jump = int(input())
solve(0)
print(visited)
print(sum(map(sum, visited)))