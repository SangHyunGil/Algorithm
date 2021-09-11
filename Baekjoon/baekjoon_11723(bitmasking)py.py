import sys
input = sys.stdin.readline


n, m = map(int, input().split())

answer = set([bin(0)])
current = [[bin(0), 0]]
if n <= m:  
    current.append([bin(2**n), n])
    answer.add(bin(2**n))

if (n-1)//3+1 <= m:
    temp = 2**n
    for i in range(0, n, 3):
        temp -= 2 **i
    current.append([bin(temp), (n-1)//3+1]) 
    answer.add(bin(temp))

print(answer)

while current:
    c, cnt = current.pop()

    if cnt + n <= m and c|d1 not in answer:
        current.append([c|d1, cnt+n])
        
    if cnt + n//2 <= m:
        if c|d2 not in answer:
            current.append([c|d2, cnt+n])
        if c|d3 not in answer:
            current.append([c|d2, cnt+n])
    if cnt + (n-1)//3+1 <= m and c|d4 not in answer:
        current.append([c|d4, cnt+n])
    