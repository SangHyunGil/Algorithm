import math
import sys
sys.setrecursionlimit(10**8)

def solution(enroll, referral, seller, amount):
    
    person = dict()
    person["root"] = ['-', 0]
    for enr, ref in zip(enroll, referral):
        if ref == '-':
            ref = "root"
        person[enr] = [ref, 0]
    
    sell = dict()
    for s, a in zip(seller, amount):
        if s in sell:
            sell[s].append(a * 100)
        else:
            sell[s] = [a * 100]
    
    for name in sell.keys():
        for cost in sell[name]:
            dfs(person, name, cost)
    
    answer = []
    for p in list(person.values())[1:]:
        answer.append(p[1])
    
    return answer

def dfs(person, name, cost):
    if name == '-' or cost == 0:
        return

    otherMoney = cost // 10
    ownMoney = cost - cost // 10

    person[name][1] += ownMoney
    dfs(person, person[name][0], otherMoney)