"""
시간을 분으로 바꾸고 이에 대한 시간을 계산해주면 된다.
만약 시간이 홀수개라면 입차를 하고 출차를 안한 상태이므로 마지막에 23:59에 해당하는 분을 추가해준다.
그리고 2개씩 짝지어 시간의 차를 구해 더해주어 최종 시간을 구한다.
최종 시간을 기준으로 요금을 계산한다.
"""
from collections import defaultdict
from math import ceil

def convertToMinutes(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

def calculateFee(total, Fees):
    limit, basic, minute, money = Fees
    result = basic
    if total > limit:
        result += ceil((total - limit) / minute) * money
    
    return result
        

def solution(fees, records):
    answer = []
    
    latest = convertToMinutes('23:59')
    cars = defaultdict(list)
    for record in records:
        time, num, types = record.split()
        minutes = convertToMinutes(time)
        cars[num].append(minutes)
    
    for car in cars:
        if len(cars[car]) % 2:
            cars[car].append(latest)

    for car in cars:
        total = 0
        carTimes = cars[car]
        for i in range(0, len(carTimes), 2):
            total += carTimes[i+1]-carTimes[i]
        
        answer.append([car, calculateFee(total, fees)])
        
    answer = [m for _, m in sorted(answer, key=lambda x : x[0])]
    
    return answer