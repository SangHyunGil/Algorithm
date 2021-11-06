import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

answer = set()

def backtracking(s, eg, n):
    if n == len(s):
        print(eg)

    else:
        for i in range(len(s)):
            if not visited[i]:
                temp = eg + s[i]
                if temp not in record:
                    visited[i] = 1
                    record.add(temp)
                    backtracking(s, temp, n+1)
                    visited[i] = 0

for i in range(int(input())):
    s = list(input().strip())
    s = "".join(sorted(s))
    visited = [0] * len(s)
    record = set()
    backtracking(s, "", 0)