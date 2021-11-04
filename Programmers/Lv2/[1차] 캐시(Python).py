"""
문자열, 숫자, 나머지로 짤라준다. (정규식 이용)
문자열, 숫자, 인덱스, 실제 문자열로 리스트에 저장해주고
해당 부분에 대해 순서대로 정렬해준다.
그리고 해당 부분에 대해 실제 문자열 부분만 추출하여 출력한다.
"""

import re

def solution(files):
    answer = []
    
    for idx, file in enumerate(files):
        result = re.split('([\d]+)', file)
        answer.append([result[0].lower(), int(result[1]), idx, file])
        
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return [ans[3] for ans in answer]