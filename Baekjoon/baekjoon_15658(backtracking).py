"""
백트래킹으로 유명한 문제 중 하나이다.
백트래킹으로 탐색하면서 연산자를 하나씩 살펴보면 된다.
"""
import sys
input = sys.stdin.readline

def calc(op, a, b):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a / b)

def backtracking(cnt, sumNum):
    global minNum, maxNum

    if cnt == N:
        minNum, maxNum = min(minNum, sumNum), max(maxNum, sumNum)
        return 
    for i in range(4):
        if opNum[i] > 0:
            opNum[i] -= 1
            backtracking(cnt+1, calc(i, sumNum, arr[cnt]))
            opNum[i] += 1


minNum, maxNum = sys.maxsize, -sys.maxsize
N = int(input())
arr = list(map(int, input().split()))
opNum = list(map(int, input().split()))

backtracking(1, arr[0])
print(maxNum)
print(minNum)