"""
단순히 생각하면 편하다.
첫번째 심은 나무가 자라려면 +2, 두번째 심은 나무가 자라려면 +3 그리고 계속 순차적으로 증가한다.
이를 덧셈을 통해 구해주고 다음과 같이 최댓값이 우리가 구하는 날이다.
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
tree = sorted(list(map(int, input().split())), reverse=True)
day = [i for i in range(2, 2+N)]
ans = [t+d for t, d in zip(tree, day)]
print(max(ans))