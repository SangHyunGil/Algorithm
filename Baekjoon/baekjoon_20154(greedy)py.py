"""
두 개씩 짝을 지어주면서 더해나가며 최종이 홀짝인지 구분하는 문제이다.
사실상 계속적으로 더해나가는 것이므로 단순 순차적으로 다 더해나가면 된다.
주의할 점은 10으로 나머지를 계속 구해야한다는 점이면 두개씩 굳이 찢으면서 하려했다가
반복문이 2번 나와 O(N^2)이 나올 수 있다는 점이다.
"""

import sys
input = sys.stdin.readline

alpha = ["A", "B", "C", "D", "E", "F", "G", "H",
         "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X",
         "Y", "Z"]
num = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

dic = {a : n for a, n in zip(alpha, num)}

sum = 0
for i in input().rstrip():
    sum += dic[i]
    sum %= 10

if sum % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")