import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

s = list(words[0])
for word in words[1:]:
  for idx, c in enumerate(word):
    if s[idx] != c:
      s[idx] = '?'

print("".join(s))