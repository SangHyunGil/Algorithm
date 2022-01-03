"""
이 문제는 덱을 이용해 구현했다.
다리 위에 존재하는 트럭들을 덱을 통해 구현해주었고 그 위에 올라가있는 무게를 따로 저장했다.
만약 트럭들을 올려놓고 단순 SUM을 활용해 이를 구한다면 O(N)의 시간복잡도로 계속 구해야하기에 이를 피했다.
그리고 트럭이 모두 지나갔는지를 확인하기 위해 각각 통과한 시간을 저장한 리스트를 생성해 트럭의 수와 비교했다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = []
    cnt, idx = 1, 1
    queue, weightSum = deque([1]), truck_weights[0]
    
    while len(answer) != len(truck_weights):
        cnt += 1
    
        if bridge_length == cnt-queue[0]:
            weightSum -= truck_weights[len(answer)]
            answer.append(queue.popleft())

        if idx < len(truck_weights) and weight >= weightSum + truck_weights[idx]:
            weightSum += truck_weights[idx]
            queue.append(cnt)
            idx += 1

    return cnt

print(solution(2, 10, [7,4,5,6]))