"""
이 문제는 그리디하게 접근하는 문제이다.
최대한 구명보트를 적게 쓰려고하면 어떻게 해야할까?
최대한 많은 사람을 2명씩 끼워서 태워야한다.
어떻게 최대한 많이 끼워서 태울 수 있을까?
무게가 가장 많이 나가는 사람들을 끼워서 태울 수 있어야 최대한 2명씩 끼워서 나갈 수 있을 것이다.
그렇다면 무게가 가장 많이 나가는 사람들을 끼우려면 어떻게 해야할까?
무게가 가장 작은 사람과 짝지으면 된다.
이런식으로 양 끝에 있는 사람들을 기준으로 묶어서 최대무게를 비교한다.
그리고 안된다면 최대무게를 가진 사람은 혼자 타고 그보다 적은 사람 중 가장 무거운 사람을 비교하면서
그리디하게 접근하면 된다.
둘이 같이 타는 경우 따로 visited 배열을 만들어 체크해주었고 체크되지 않은 수만큼 더하여 정답을 구했다.
(단순 len(people) - answer 도 가능하다.)
"""
def solution(people, limit):
    answer = 0
    people.sort()
    visited = [0] * len(people)
    left, right = 0, len(people)-1
    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            visited[left], visited[right] = 1, 1
            left += 1
            
        right -= 1    
    
    return answer + visited.count(0)