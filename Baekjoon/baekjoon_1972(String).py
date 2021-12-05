import sys
input = sys.stdin.readline

H, Y = map(int, input().split())
MONEY = [H] + [0] * 10

for i in range(1, Y+1):
    MONEY[i] = MONEY[i-1]*1.05

    if i >= 3:
        MONEY[i] = max(MONEY[i], MONEY[i-3]*1.2)
    if i >= 5:
        MONEY[i] = max(MONEY[i], MONEY[i-5]*1.35)
    MONEY[i] = int(MONEY[i])
    print(MONEY)
print(int(MONEY[Y]))