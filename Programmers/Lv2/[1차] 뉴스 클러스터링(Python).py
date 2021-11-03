"""
모든 문자열을 소문자로 변경한다.
각각에 대해 특수문자를 제외한 문자를 2개씩 나누어준다.
각각에 대한 합집합과 차집합을 구한다.
분모가 0이라면, 65536 (합집합이 0이라면 차집합 또한 0일 것이다.)
분모가 0이 아니라면, 65536을 곱하고 내림한다.
"""

from collections import Counter

def isAlpha(a, b):
    return 'a' <= a <= 'z' and 'a' <= b <= 'z'

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    s1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if isAlpha(str1[i], str1[i+1])]) 
    s2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if isAlpha(str2[i], str2[i+1])])

    numerator = sum((s1 & s2).values())
    denominator = sum((s1 | s2).values())

    if denominator:
        result = numerator / denominator
        return int(result * 65536)
    else:
        return 65536