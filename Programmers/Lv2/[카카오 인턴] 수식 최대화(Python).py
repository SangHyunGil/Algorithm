"""
먼저, 산술연산기호를 기준으로 나누어준다.
그리고 연산식의 길이가 1000이므로 충분히 산술연산기호 3개를 브루트 포스로 돌릴 수 있다.
그에 따라, 브루트 포스로 돌린 뒤 가장 높은 값을 찾는다.
"""

import re
from itertools import permutations

def solution(expression):
    answer = 0
    expression = re.split('([\D])', expression)
    
    for comb in permutations("*+-", 3):
        exp = expression[:]
        for t in comb:
            while t in exp:
                i = exp.index(t)
                exp[i-1:i+2] = [str(eval("".join(exp[i-1:i+2])))]

        answer = max(answer, abs(int(exp[0])))

    return answer

solution("100-200*300-500+20")
    

