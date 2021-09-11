import sys
input = sys.stdin.readline

S = ['0'] * 20
for _ in range(int(input())):
    command = input().strip().split()

    if len(command) == 1:
        if command[0] == 'all':
            S = ['1'] * 20
        else:
            S = ['0'] * 20


    else:
        if command[0] == 'add':
            S[int(command[1])-1] = '1'
        elif command[0] == 'check':
            print(1 if S[int(command[1])-1] == '1' else 0)
        elif command[0] == 'toggle':
            S[int(command[1])-1] = '0' if S[int(command[1])-1] == '1' else '1'
        else:
            S[int(command[1])-1] = '0'

