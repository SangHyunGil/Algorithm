import re
from itertools import combinations
from collections import defaultdict

language = {'-' : 0, 'cpp' : 1, 'java' : 2, 'python' : 3}
skill = {'-' : 0, 'backend' : 1, 'frontend' : 2}
exprience = {'-' : 0, 'junior' : 1, 'senior' : 2}
soulfood = {'-' : 0, 'chicken' : 1, 'pizza' : 2}

def makeCategory(info):
    category = defaultdict(list)
    for inf in info:
        result = re.split('\s', inf)
        condition, score = result[:-1], result[-1]
        for i in range(5):
            for comb in combinations(condition, i):
                temp = "".join(comb)
                if temp in category:
                    category[temp].append(int(score))
                else:
                    category[temp] += 1
    print(category)
    return

def solution(info, query):
    answer = []
    makeCategory(info)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])