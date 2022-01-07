"""
처음 시도로 단순 브루트 포스로 진행하였다.
이는 257(높이) * 500 * 500(배열)의 복잡도로 구성되기에 1초안에 가능하다고 생각했다.
다른 언어의 경우 통과가 잘 되었지만 파이썬의 경우 통과가 되지 않았다.
Pypy3의 경우에도 통과가 잘 되지 않아 코드를 조금 수정했다.
단순 체크로직을 Main에서 처리하는 것이 아니라 Method로 추출해 처리하는 방식을 이용했다.
이전에 어떤 로직을 메소드로 추출해 진행하는 것이 더 빠르다는 것이 생각나 진행해보았더니
아슬아슬하게 통과되었다.
코드를 좀 더 개선하기 위해 시간 복잡도를 줄이는 방법을 강구하던 도중 새로운 방법을 시도해보았다.
같은 높이를 가진 경우 모두 같은 시간을 요구할 것이므로 같은 높이를 서로 묶어 이를 처리할 수 있도록 하였다.
같은 높이의 경우 같은 dict에 묶어 이를 저장하여 시간을 계산하였다.
이를 처리하니 간단하게 Python 제출에도 AC를 받을 수 있었다.
"""
import sys
from collections import Counter

input = sys.stdin.readline
# 새로운 코드
def check():
    ans, copyB = 0, B
    for k, v in dic.items():
            if k > block:
                copyB += (k - block) * v
                ans += 2 * (k - block) * v
            else:
                copyB += (k - block) * v
                ans += (-k + block) * v

    return ans, copyB

minTime, minBlock = sys.maxsize, -1
N, M, B = map(int, input().split())
graph = []
for _ in range(N):
    graph += map(int, input().split())
dic = dict(Counter(graph))

for block in range(257):
    ans, copyB = check()
    
    if copyB >= 0 and minTime >= ans:
        minTime, minBlock = ans, block

print(minTime, minBlock)

# 이전 코드
# def check():
#     ans, copyB = 0, B
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] > block:
#                 copyB += graph[i][j] - block
#                 ans += 2 * (graph[i][j] - block)
#             else:
#                 copyB += graph[i][j] - block
#                 ans += -graph[i][j] + block
    
#     return ans, copyB

# minTime, minBlock = sys.maxsize, -1
# N, M, B = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# for block in range(257):
#     ans, copyB = check()
    
#     if copyB >= 0 and minTime >= ans:
#         minTime, minBlock = ans, block

# print(minTime, minBlock)