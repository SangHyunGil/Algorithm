import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
weight.sort()

w_sum = 0
for w in weight:
    if w_sum+1 < w: break
    w_sum += w
print(w_sum+1)