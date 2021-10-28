def solution(s, n):
    answer = ''
    for c in s:
        answer += chr(ord(c)+n)

    return answer