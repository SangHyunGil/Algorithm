"""
조합을 활용한 문제이다.
총 3가지의 물건까지 담을 수 있다고 했으므로
우리가 확인해야할 경우의 수는 다음과 같다.
5C1, 5C2, 5C3 
이에 대한 시간 복잡도를 살펴보면
N, N^2, N^3
N은 5000까지이므로 N^3은 불가능하다.
그래서 우리는 2가지까지 확인하면서 이를 해결할 방법을 찾아야한다.
2가지의 경우의 수를 구하고 총 무게에서 뺀 뒤 해당 부분이 있는지를 확인하면 된다.
dict로 구현할 경우 있는지 확인하는 것은 O(1)이므로 충분히 이 안에 해결이 가능하다.
아니면 2가지의 경우의 수를 구하고 이분탐색으로 log(N)으로 해결할 방법도 있을 것 같다.
하지만 시간이 여유롭지 못한 파이썬의 경우 실패할 것이라고 예상되어 전자의 방법을 택했다.
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
d = dict.fromkeys([*map(int, input().split())], 1)
print(solve())