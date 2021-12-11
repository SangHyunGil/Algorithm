import sys
input = sys.stdin.readline
 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    num = arr[0]
    for k in arr:
        num = gcd(num, k)
        print(num, gcd(4, 4))

 
    if num == 1:
        print("true")
    else:
        print("false")