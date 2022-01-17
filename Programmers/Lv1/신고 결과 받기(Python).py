"""
단순히 Map을 이용해서 풀었다.
신고를 하는 사람과 신고를 받는 사람을 나누어 정리하면 된다.
그리고 최종적으로 신고를 하는 사람을 루프로 돌려 신고를 한 사람이 K번 이상 신고를
받았는지 확인하고 이를 처리해주면 된다.
"""

def solution(id_list, report, k):
    answer = []
    dic = dict()
    ban = dict()
    
    for i in id_list:
        dic[i] = set()
        ban[i] = set()
        
    for r in report:
        reporter, reportee = r.split()
        dic[reporter].add(reportee)
        ban[reportee].add(reporter)
    
    for i in id_list:
        temp = 0
        for v in dic[i]:
            if len(ban[v]) >= k:
                temp += 1
        answer.append(temp)
    
    return answer