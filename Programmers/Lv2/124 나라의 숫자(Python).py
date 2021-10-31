from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    print(scoville)
    while scoville[0] <= K:
        answer += 1
        print(scoville, answer)
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))