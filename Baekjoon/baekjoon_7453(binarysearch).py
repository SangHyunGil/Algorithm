"""
단순 브루트 포스하게 접근하면 O(N^4)으로 불가능하다.
이를 단순화하기 위해 Meet In The Middle을 이용해보자.
4개의 원소를 가진 배열을 2개씩 쪼개 합을 구한 뒤 이에 대한 부분을 구하자.
그러면 각각에 대해 O(N^2), O(N^2)으로 풀어낼 수 있다.
그리고 이에 대한 합을 구하면 되는데 이 부분에 대해 이분탐색으로 진행하려했다.
그러면 최종적으로 O(N^2logn)이 되나 파이썬의 문제인지 해결이 잘 되지 않았다.
이에 대한 해결책으로 Map을 이용하여 접근하여 풀었다.
"""

import sys
input = sys.stdin.readline

ans = 0
n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a), B.append(b), C.append(c), D.append(d)

dic = dict()
for i in range(n):
    for j in range(n):
        s = A[i] + B[j]
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

for i in range(n):
    for j in range(n):
        s = -(C[i] + D[j])
        if s in dic:
            ans += dic[s]

print(ans)

# def lower_bound(i):
#     left, right = 0, n*n

#     while left < right:
#         mid = (left + right) // 2
#         if lsum[i] + rsum[mid] < 0:
#             left = mid + 1
#         else:
#             right = mid

#     return right

# def upper_bound(i):
#     left, right = 0, n*n

#     while left < right:
#         mid = (left + right) // 2
#         if lsum[i] + rsum[mid] <= 0:
#             left = mid + 1
#         else:
#             right = mid

#     return right

# ans = 0
# n = int(input())
# A, B, C, D = [], [], [], []
# for i in range(n):
#     a, b, c, d = map(int, input().split())
#     A.append(a), B.append(b), C.append(c), D.append(d)

# lsum, rsum = [], []
# for i in range(n):
#     for j in range(n):
#         lsum.append(A[i] + B[j])
#         rsum.append(C[i] + D[j])

# rsum.sort()
# for i in range(n*n):
#     lb = lower_bound(i)
#     rb = upper_bound(i)
#     ans += rb-lb

# print(ans)