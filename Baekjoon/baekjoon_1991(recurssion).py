import sys
input = sys.stdin.readline

ans = 0
def solve(i, cnt):
    global ans
    if cnt == len(n):
        ans += 1
        return

    solve(i+1, cnt+1)
    if i < len(n)-1 and int(n[i]+n[i+1]) <= 26:
        solve(i+2, cnt+2)

n = list(input().rstrip())
solve(0, 0)
print(ans)
