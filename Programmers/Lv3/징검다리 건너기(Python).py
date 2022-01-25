"""
단순 이중 반복문으로도 해결이 가능하다. (몇명 건널지, 해당 명수가 가능한지)
하지만 이렇게 된다면 시간초과가 난다.
그러기에 명수에 대한 부분을 로그복잡도로 줄여보자.
그러기 위해서 이분탐색을 진행해보면 된다.
"""

def solution(stones, k):
    left, right = 0, 200000001
    while left <= right:
        mid = (left + right) // 2
        
        temp, space = 0, 0
        for i in range(len(stones)):
            if stones[i] < mid:
                space += 1
                temp = max(temp, space)
            else:
                space = 0
        
        if temp < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left-1