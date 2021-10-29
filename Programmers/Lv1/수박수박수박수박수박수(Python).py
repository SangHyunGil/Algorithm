def solution(n):
    # 기본 배수
    pattern = "수박" * (n//2)
    # 나머지 문자
    pattern += "수" if n % 2 else ""
    return pattern