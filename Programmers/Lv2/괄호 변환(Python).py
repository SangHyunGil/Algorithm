import re
from itertools import permutations

def solution(expression):
    answer = 0
    expression = re.split('([\D])', expression)
    
    for comb in permutations("*+-", 3):
        temp = expression[:]
        for t in comb:
            while t in temp:
                i = temp.index(t)
                temp[i-1:i+2] = [str(eval("".join(temp[i-1:i+2])))]

        answer = max(answer, abs(int(temp[0])))

    return answer

solution("100-200*300-500+20")
    

