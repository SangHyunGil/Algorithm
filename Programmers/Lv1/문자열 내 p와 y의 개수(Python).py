def solution(s):
    # 소문자로 변경
    s = s.lower()

    # p, y 카운트 후 개수 비교
    return True if s.count('p') == s.count('y') else False