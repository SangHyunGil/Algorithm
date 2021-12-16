"""
구현과 시뮬레이션을 이용한 문제이다.
이는 R, C가 각각 10이하이므로 충분히 구현과 시뮬레이션을 이용해도 된다.
이 부분을 구하기 위해서는 전체 섬 주변에 바다가 3이상인지를 확인하고 
지도를 복사한 뒤 해당 부분에 표시해주면 된다.
지도를 복사하는 이유는 계속적으로 원래 지도에 갱신하면 섬이 바다로 바뀐 부분이 영향을 줄 수 있기 때문이다.
그리고 주의할 점은 지도뿐 아니라 지도 밖의 부분도 바다라고 생각하고 이를 진행해야한다는 점이다.
그리고 직사각형을 출력하는데 있어 x, y 좌표의 각각 최대 최소를 구해 출력해주면 된다.
"""

import sys
from itertools import combinations
input = sys.stdin.readline

def solve():
    for x, y in combinations(d.keys(), 2):
        if x == C or y == C:
            return 1

        elif x+y == C:
            return 1
        
        else:
            temp = (C-x-y)
            if temp in d and temp != x and temp != y:
                return 1   

    return 0


N, C = map(int, input().split())
arr = [*map(int, input().split())]
d = dict.fromkeys(arr, 1)
print(d)
print(solve())