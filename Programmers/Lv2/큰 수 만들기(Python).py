"""
숫자가 가장 크게 만드는 문제이다.
숫자를 가장 크게 만드려면, 최대한 앞의 자리수가 크게 만들어야한다.
그렇다면, 우리는 스택으로 앞에서부터 넣으면서 더 큰 수가 존재한다면 앞에 존재하는 작은 수를 제거하고 추가하면 된다.
이러한 방식으로 진행하다가 k가 없다면 루프를 종료시킨다.
만약 k가 남는다면 앞에서부터 k개를 출력한다.
"""

def solution(number, k):
    stack = []
    
    for num in number:
        if stack and k > 0:
            while stack and k and stack[-1] < num:
                stack.pop()
                k -= 1
            stack.append(num)
        else:
            stack.append(num)

    return "".join(stack)[:-k] if k else "".join(stack)