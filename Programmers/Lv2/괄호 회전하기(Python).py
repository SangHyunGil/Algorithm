"""
스택의 대표적인 문제 중 하나인 올바른 괄호 확인하기이다.
다만 다른점은 왼쪽으로 Shift하면서 올바른 괄호가 몇 개인지 카운트하는 것이다.
이 부분에 대해서는 Python에서 지원하는 Slicing을 활용해 구현하면 된다.
"""
def isCorrect(s):
    stack = []
    
    for c in s:
        if stack:
            if stack[-1] == "[" and c == "]":
                stack.pop()
            elif stack[-1] == "(" and c == ")":
                stack.pop()
            elif stack[-1] == "{" and c == "}":
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
            
    return len(stack) == 0

def solution(s):
    answer = 0
    for i in range(len(s)):
        ns = s[i:] + s[:i]
        answer += isCorrect(ns)
    return answer