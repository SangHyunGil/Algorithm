import re

def solution(numbers):
    return re.search("[0-9]+", numbers)

print(solution("a234"))