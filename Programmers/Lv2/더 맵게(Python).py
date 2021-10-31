"""
힙을 사용하여 최소인 두 값을 계속적으로 변환하여 K 이상인지 확인한다.
제일 작은 수가 K 이상이라면 중지한다.
만약, 힙의 총 개수가 1개라면 중지한다.
결과에 대해서는 힙의 최솟값을 기반으로 확인한다.
"""

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
    
    return answer if scoville[0] >= K else -1
