"""
유일성을 만족하는 키들을 모두 구한다.
유일성을 만족하는 키 중 최소성을 만족하는 키를 구하려면 부분집합에 포함되는지를 확인하면 된다.
부분집합을 확인하는데 있어, 가장 적은 키를 포함하는 부분부터 진행해야한다.
아니라면 최소성을 만족시키지 못하는 경우도 발생한다.
"""

from itertools import combinations

def isCandidate(answer_set, cb):
    for i in range(1, len(cb)+1):
        for c in combinations(cb, i):
            if c in answer_set:
                return False

    return True

def solution(relation):
    answer = 0
    
    answer_set = set()
    for i in range(1, len(relation[0])+1):
        for cb in combinations(range(len(relation[0])), i):
            check = set()
            length = len(relation)
            for rel in relation:
                tp = tuple(rel[i] for i in cb)
                check.add(tp)
            
            if len(check) == length and isCandidate(answer_set, cb):
                answer += 1
                answer_set.add(tuple(cb))
        
    return answer