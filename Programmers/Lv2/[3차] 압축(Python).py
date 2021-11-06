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
