"""
이 문제도 천천히 해당 문제를 구현하면 된다.
단, 주의해야할 점은 #이 붙어있는 음이 있다는 점이다.
C, C#을 비교할 때 헷갈리면 안되기 때문에 C#과 같은 #음을 임의의 값으로 변경해준다.
해당 임의의 값으로 변경해준 뒤, 총 시간을 구한다.
총 시간만큼 멜로디를 반복 연주해주기 위해 산술연산을 이용해준다.
그리고 m이 멜로디 안에 포함되는지 확인한다.
그리고 포함된다면 리스트 안에 넣고 최종적으로 시간, 인덱스를 기준으로 정렬하여 정답을 도출한다.
"""

import re

def changeMelody(melody):
    melody = melody.replace('A#', 'a')\
                   .replace('C#', 'b')\
                   .replace('D#', 'c')\
                   .replace('F#', 'd')\
                   .replace('G#', 'e')
    
    return melody

def getMinutes(musicinfo):
    start = list(map(int, musicinfo[0].split(':')))
    end = list(map(int, musicinfo[1].split(':')))
    minutes = (end[0] - start[0]) * 60 + end[1] - start[1]
    
    return minutes
    
def makeFullMelody(minutes, melody):
    length = len(melody)
    if minutes > length:
        return melody * (minutes//length) + melody[:minutes%length]
    else:
        return melody[:minutes]
    
def solution(m, musicinfos):
    answer = []
    m = changeMelody(m)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = re.split(',', musicinfo)
        
        melody = changeMelody(musicinfo[3])
        minutes = getMinutes(musicinfo)
        fullMelody = makeFullMelody(minutes, melody)

        if m in fullMelody:
            answer.append([minutes, idx, musicinfo[2]])
    
    answer.sort(key=lambda x : (-x[0], x[1]))
    return answer[0][2] if answer else "(None)"