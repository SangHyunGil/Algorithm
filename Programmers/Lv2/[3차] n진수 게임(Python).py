"""
진법과 반복을 활용한 문제이다.
진법 변환에 있어서 10~15는 알파벳 대문자로 나타내야하고 0~9는 숫자로 나타내야한다.
나머지 부분에 대해 해당 부분을 매칭해주기 위한 dic을 선언하였다.
그리고 진법변환 결과를 반환해준다.
해당 결과를 이어 붙여 나가면서 길이가 채워졌다면 리턴한다.
"""

def makeNth(n, m):
    s = ""
    dic = "0123456789ABCDEF"
    if m == 0:
        return str(0)
    
    while m:
        s = dic[m % n] + s
        m //= n
    
    return s

def findNumbers(n, t, m, p):
    cnt = 0
    ans = ""
    while len(ans)//m < t:
        ans += makeNth(n, cnt)
        cnt += 1
    
    return ans[p-1::m][:t]

def solution(n, t, m, p):
    return findNumbers(n, t, m, p)

solution(16,16,2,2)
