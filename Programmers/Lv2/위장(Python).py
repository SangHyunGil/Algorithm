"""
먼저, 옷의 종류(Category)에 따라 옷(Cloth)을 저장해준다.
그리고 경우의 수를 공식을 통해 구해준다.
상의 n개, 하의 m개 : (n+1) * (m+1) - 1
"""

from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    for name, category in clothes:
        dic[category].append(name)
    
    for d in dic:
        answer *= len(dic[d])+1
        
    return answer-1