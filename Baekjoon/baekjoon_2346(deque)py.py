import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    answer = [0]
    k = 1
    for i in range(n):
        answer.append(answer[-1] | k)
        k += 1

    k = 1
    for i in range(n-1):
        answer.append(answer[-1] ^ k)
        k = k << 1

    print(*list(map(bin, answer)))
    print(*answer)