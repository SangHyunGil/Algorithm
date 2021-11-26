"""
순서를 어기면 안된다라는 점에 주목하자.
이 말은 즉, 어떤 스킬은 해당 선행스킬을 하기전에 나올 수 없다는 것이다.
그리고 스킬은 중복되지 않는다는 점에 주목하자.
스킬은 중복되지 않으므로 한번 나오면 더이상 나오지 않으므로 순차적으로 나온 스킬들을 지워나가고
순차적으로 탐색하며 배운 스킬을 지워나간 뒤, 스킬이 전부 남아있지 않다면 모든 스킬을 배운 것이다.
하지만 배우려는 스킬과 스킬트리의 맨 앞 스킬이 일치하지 않는다면 스킬트리를 어긴 것이다.
이를 for-else 구문을 통해 구현하였다.
"""

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        queue = deque(list(skill))
        for st in skill_tree:
            if st in queue:
                if queue.popleft() != st:
                    break
                
        else:
            answer += 1
                
    
    return answer