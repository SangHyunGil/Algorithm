def solution(citations):
    citations.sort(reverse=True)
    print(list(map(min, (enumerate(citations, start=1)))))
    return citations[len(citations)//2]

solution([3,0,5,6,1])