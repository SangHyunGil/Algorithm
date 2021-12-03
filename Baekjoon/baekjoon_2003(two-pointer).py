import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
total = arr[0]
left, right = 0, 1
while left <= right:
    if total == m:
        answer += 1
        total -= arr[left]
        left += 1

    if right == n and total < m:
        break

    elif total < m:
        total += arr[right]
        right += 1

    else:
        total -= arr[left]
        left += 1

print(answer)