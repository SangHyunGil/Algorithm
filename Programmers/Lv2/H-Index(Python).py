"""
먼저, 정렬을 진행한다.
오름차순으로 루프를 진행하면 아래 인덱스들은 모두 h번 이하 인용이므로 조건을 만족한다.
따라서 확인해야할 부분은 오직 "h편 이상"인지이다.
그래서 그 부분에 대한 조건만 확인하면된다.
"""

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0