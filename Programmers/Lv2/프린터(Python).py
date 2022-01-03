"""
단순 스택과 큐를 이용한 문제이다.
먼저 우선순위에 따라 프린트를 하고 제거해야하므로 우선순위를 오름차순을 정렬해준다.
그리고 우선순위가 같은 경우가 존재하므로 같은 경우에서 몇 번째인지를 구분하기 위해 인덱스를 함께 저장하는 리스트를
만들어준다.
그리고 반복문을 돌면서 우선순위가 높은 것을 순차적으로 제거하며 몇 번째로 제거되는지 찾는다.
"""

from heapq import heappop, heappush, heapify
from collections import deque

def solution(priorities, location):
    answer = 1
    printer = deque([[prior, idx] for idx, prior in enumerate(priorities)])
    priorities.sort()
    
        
    while True:
        if printer[0][0] == priorities[-1]:
            if printer[0][1] == location:
                return answer
            else:
                answer += 1
                printer.popleft()
                priorities.pop()
        else:
            printer.append(printer.popleft())