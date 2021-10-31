"""
단순히 numbers를 dfs로 탐색하면서 target 값을 완성시킬 수 있는지 확인한다.
"""

answer = 0

def dfs(value, target, numbers, cnt):
    global answer
    if cnt == len(numbers):
        if value == target:
            answer += 1
        return

    dfs(value-numbers[cnt], target, numbers, cnt+1)
    dfs(value+numbers[cnt], target, numbers, cnt+1)


def solution(numbers, target):
    dfs(0, target, numbers, 0)
    return answer