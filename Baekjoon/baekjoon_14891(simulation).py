"""
큰 알고리즘이 필요한 부분은 없고 단순 구현문제이다.
이 문제를 풀면서 필요한 부분은 다음과 같다.
배열의 로테이션, 로테이션에 대한 전파이다.
어떤 한 톱니가 회전하게 되면 배열 자체가 로테이션된다는 뜻이고 그 옆에 톱니에게 전파가 된다.
이러한 부분을 구현하기 위해서 로테이션을 진행하는 메소드를 하나 구현했고
왼쪽으로 전파하는 부분, 오른쪽으로 전파하는 부분에 대해 재귀를 통해 구현했다.
이러한 부분은 동시다발적으로 일어나므로 배열의 로테이션에 대한 이펙트가 같은 사이클에 전파되면 안된다.
그러기에 로테이션을 어떻게 해야하는지에 대한 정보를 담는 리스트를 만들어 저장하고
모든 과정이 끝나고 로테이션을 진행한다.
점수를 구하는 과정 자체는 2**(idx-1)에 1일 경우에만 곱하면 되므로 이 로직을 통해 점수를 구했다.
"""
import sys
input = sys.stdin.readline

def rotate(i, d):
    if d == 1:
        gear[i] = [gear[i][-1]] + gear[i][:-1]
    else:
        gear[i] = gear[i][1:] + [gear[i][0]]

def left(i, d):
    if i >= 1 and gear[i][6] != gear[i-1][2]:
        rt[i-1] = d * -1
        left(i-1, d * -1)

def right(i, d):
    if i <= 2 and gear[i][2] != gear[i+1][6]:
        rt[i+1] = d * -1
        right(i+1, d*-1)

command = []
gear = [list(input().rstrip()) for _ in range(4)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    command.append([a-1, b])

for i, d in command:
    rt = [0, 0, 0, 0]
    rt[i] = d
    left(i, d)
    right(i, d)
    
    for idx, r in enumerate(rt):
        if r:
            rotate(idx, r)
    
answer = 0
for idx, g in enumerate(gear):
    answer += int(g[0]) * (2**(idx))
print(answer)