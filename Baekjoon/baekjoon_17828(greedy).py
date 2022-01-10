"""
숫자의 길이가 5백만이고 알파벳 자체가 26개이다.
그에 따라, 26개씩 일일히 전부 해보는 방식은 절대 시간안에 들어올 수 없고
어떨 때 "사전상 가장 앞"이 될지를 생각해보자.
앞에가 "작을수록" 사전상 앞에 올 것이다.
불가능한 경우는 가장큰 26인 알파벳으로 전부 채워도 되지 않을 경우이다.
위의 사안들을 고려하여 구현해보자.
먼저, 불가능한 경우인지 체크한다.
그리고 현재 남은 길이의 -1하여 몇으로 채워야할지 고민한다.
26 * N-1이 26보다 크다면 A로 채워도 무방하다. (충분히 A로 채워도 채울 수 있다.)
아니라면 그 수는 A가 아닌 다른 수로 채워야한다.
그러기 위해 빼주면 된다.
"""
import sys
input = sys.stdin.readline

alpha = {i+1 : chr(ord('A')+i) for i in range(26)}
answer = []
N, M = map(int, input().split())   

if N > M or M > 26 * N:
    print("!")
    
else:
    while N:
        res = 26 * (N-1)
        if M < res:
            answer.append(alpha[1])
            M -= 1
        else:
            answer.append(alpha[M-res])
            M = res
        N -= 1

    print("".join(answer))