import sys
input = sys.stdin.readline

def solve():   
    for k in range(int(input())):
        n = int(input())
        result = "YES"
        tel = sorted([input().strip() for _ in range(n)])
        print(tel)
        for i in range(n-1):
            if tel[i] == tel[i+1][:len(tel[i])]:
                result = "NO"

        print(result)

solve()