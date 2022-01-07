"""
이분탐색으로 진행하는 문제이다.
이분탐색을 이용하지 않는다면 N개 중 M개를 골라 거리를 계산해야한다.
이를 달리 생각하면 N개 중 제외할 M개를 골라 거리를 계산하면 된다.
조합을 이용하면서 거리를 계산하니 시간초과가 날 것임이 분명했다.
그래서 조합을 이용하는 것 대신 이분 탐색을 이용하고자 하였다.
뛰는 범위 자체를 이분 탐색하여 해당 범위 아래에 있는 것들을 제거하는 것으로 하여 진행한다.
그리고 제거되는 것이 M과 M보다 작다면 갱신한다.
M보다 작은 이유는 어떤 경우에 있어 하나도 제거가 안되는 경우가 존재한다. 25, 3, 1 [2 11 13]
"""
import sys
input = sys.stdin.readline

D, N, M = map(int, input().split())
rock = [int(input()) for i in range(N)]
arr = [0] + sorted(rock) + [D]

answer = -sys.maxsize
left, right = 0, D
while left <= right:
    mid = (left + right) // 2

    cnt, postIdx = 0, 0
    for idx in range(1, N+2):
        if arr[idx] - arr[postIdx] < mid:
            cnt += 1
        else:
            postIdx = idx
    
    if cnt > M:
        right = mid - 1 

    elif cnt < M:
        left = mid + 1

    else:
        answer = max(answer, mid)
        left = mid + 1
        
print(answer)