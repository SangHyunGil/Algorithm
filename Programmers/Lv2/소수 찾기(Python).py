"""
이 문제는 브루트 포스로도 충분히 해결가능한 문제이다.
따라서, 순열을 통해 만들 수 있는 모든 숫자의 조합을 만든다.
다만, 순열이므로 중복되는 부분에 대해 제거하기 위한 set으로 제거해준다.
그리고 에라토스테네스의 체로 소수가 아닌 부분을 제거하여 소수인 부분만 남겨준다.
"""

from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)