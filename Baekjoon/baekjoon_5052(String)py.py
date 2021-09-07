import sys
input = sys.stdin.readline

def getPI(PI):
    left = 0
    for right in range(1, len(P)):
        while left > 0 and P[left] != P[right]:
            left -= 1
        
        if P[left] == P[right]:
            left += 1
            PI[right] = left
    
    return PI

def KMP():
    left = 0
    for right in range(len(T)):
        while left > 0 and P[left] != T[right]:
            left = PI[left-1]
        
        if P[left] == T[right]:
            if left == len(P)-1:
                answer[0] += 1
                answer[1].append(right-len(P)+2)
                left = PI[left]
            else:
                left += 1

        

answer = [0, []]
T = input().strip()
P = input().strip()
PI = getPI([0 for _ in range(len(P))])
KMP()
print(answer[0])
print(*answer[1])
