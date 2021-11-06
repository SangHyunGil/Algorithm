"""
전형적인 스택 문제 중 하나인 괄호문제이다.
스택에 넣으면서 조건에 만족하면 pop하는 식으로 진행한다.
"""

def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)

    return False if stack else True