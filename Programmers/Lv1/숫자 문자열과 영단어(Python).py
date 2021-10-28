import sys
input = sys.stdin.readline

def solution(s):
    # 숫자 맵
    number = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
        "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

    # 영어 -> 숫자
    for num in number:
        if num in s:
            s = s.replace(num, str(number[num]))

    return s

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))