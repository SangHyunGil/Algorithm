import math
from itertools import combinations
def solution(nums):
    answer = 0
    
    prime = [False, False] + [True] * 3000
    for i in range(2, int(math.sqrt(3000))):
        if prime:
            for j in range(i+i, 3000, i):
                prime[j] = False

    for comb in combinations(nums, 3):
        if prime[sum(comb)]:
            answer += 1

    return answer

print(solution([1, 2, 3, 4]))