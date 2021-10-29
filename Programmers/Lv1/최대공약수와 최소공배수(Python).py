# 유클리드 호제법
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

def solution(n, m):
    answer = []
    # 최대 공약수
    answer.append(gcd(n,m))
    # 최대 공배수
    answer.append(n*m//gcd(n,m))
    return answer