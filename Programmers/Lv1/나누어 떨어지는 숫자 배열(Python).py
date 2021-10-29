import math

def solution(n):
    prime = [False, False] + [True] * 200
    for i in range(2, int(math.sqrt(200))):
        if prime[i]:
            for j in range(i+i, 200, i):
                prime[j] = False

    return n-1

solution(11)