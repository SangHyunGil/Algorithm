"""
각 원소에 대해 phone의 길이로 정렬하여 각 phone이 접두사로 사용되는지 확인한다.
중복의 여부를 확인하기 위해 set을 활용하여 속도를 올렸다.
1,000,000 * 20 = 20,000,000 이라 충분히 시간안에 들어온다.
"""

def solution(phone_book):
    phone_book.sort(key= lambda x : len(x))

    store = set([phone_book[0]])
    for phone in phone_book[1:]:
        for i in range(len(phone)+1):         
            if phone[:i+1] in store:
                return False
        store.add(phone)
    return True