"""
4로 나눈 나머지에 2로 나눈 나머지에 대한 값이 존재한다면 실패한다.
아니라면 4의 몫을 AAAA로 2의 몫을 BB로 출력하면 된다.
"""
import sys
input = sys.stdin.readline

ans = []
boards = input().rstrip().split('.')
for board in boards:
    a, b = divmod(len(board), 4)
    c, d = divmod(b, 2)

    if d % 2:
        print(-1)
        sys.exit()
    else:
        ans.append(a * "AAAA" + c * "BB")

print(".".join(ans))