"""
최고 높이를 기준으로 왼쪽 오른쪽을 계산하면 되는 문제이다.
그 과정을 스택으로 풀어 하나씩 넓이를 계산해나가면 된다.
"""
import sys
input = sys.stdin.readline

board = [0] * 1001
endIdx = 0
maxLength, maxHeight = 0, 0
n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  board[a] = b
  if maxHeight < b:
    maxLength = a
    maxHeight = b
  endIdx = max(endIdx, a)

ans = 0
stack = []
for i in range(0, maxLength):
  if stack:
    if stack[-1] < board[i]:
      stack.pop()
      stack.append(board[i])
    ans += stack[-1]
       
  else:
    stack.append(board[i])
    ans += stack[-1]

stack = []
for i in range(endIdx, maxLength-1, -1):
  if stack:
    if stack[-1] < board[i]:
      stack.pop()
      stack.append(board[i])
    ans += stack[-1]
       
  else:
    stack.append(board[i])
    ans += stack[-1]

print(ans)