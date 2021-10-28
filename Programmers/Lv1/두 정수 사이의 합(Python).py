import math

def solution(n):
    prime = [False, False] + [True] * 1000000 
    for i in range(2, int(math.sqrt(1000001))):
        if prime[i]:
            for j in range(i+i, 1000001, i):
                print(i, j)
                prime[j] = False

    return sum(prime[:n+1])

print(solution(10))