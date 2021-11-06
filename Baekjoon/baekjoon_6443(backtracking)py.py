import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline



def backtracking(total):
    global answer

    if len(energy) == 2:
        answer = max(answer, total)

    else:
        for i in range(1, len(energy)-1):
            temp = energy[i]
            eg = energy[i-1]*energy[i+1]
            del energy[i]
            backtracking(total+eg)
            energy.insert(i, temp)
            

n = int(input())
answer = 0
energy = list(map(int, input().split()))

backtracking(0)
print(answer)
