import sys
input = sys.stdin.readline

n = int(input())

ans = 0
temp = set()
for _ in range(n):
    a, b = map(int, input().split())
    if b == 0:
        ans += len(temp)
        temp = set()
    else:
        temp.add(b)

print(ans+len(temp))