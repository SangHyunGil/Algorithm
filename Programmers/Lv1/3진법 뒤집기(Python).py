# 3진법 후 Reverse
def reversedTernary(n):
    s = ""
    while n:
        s += str(n%3)
        n //= 3

    return reversed(s)

# 10진법
def decimal(s):
    answer = 0
    for idx, c in enumerate(s):
        answer += int(c) * (3 ** idx)

    return answer
    
def solution(n):
    s = reversedTernary(n)
    answer = decimal(s)
    return answer