def solution(s, n):
    answer = ''
    for c in s:
        result = ord(c)+n
        if c.isupper():
            answer += chr(ord('A')+(result-ord('Z'))-1) if result > ord('Z') else chr(ord(c)+n)
        elif c.islower():
            answer += chr(ord('a')+(result-ord('z'))-1) if result > ord('z') else chr(ord(c)+n)
        else:
            answer += c
    return answer