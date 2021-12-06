import sys,time
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

A, T, X = [int(input()) for _ in range(3)]

def solve():
    k = 2
    cnt_0, cnt_1 = 0, 0
    answer = []
    while True:
        for i in range(0, 4):
            if i % 2:
                cnt_1 += 1
            else:
                cnt_0 += 1

            if X == 0 and cnt_0 == T:
                return (cnt_0 + cnt_1) % A
            
            if X == 1 and cnt_1 == T:
                return (cnt_0 + cnt_1) % A

        
        for i in range(0, k):
            cnt_0 += 1

            if X == 0 and cnt_0 == T:
                return (cnt_0 + cnt_1) % A

        for i in range(0, k):
            cnt_1 += 1

            if X == 1 and cnt_1 == T:
                return (cnt_0 + cnt_1) % A

        k += 1
print(solve())    