def solution(nums):
    # 폰켓몬 종류 개수
    kinds = len(set(nums))
    # 폰켓몬 선택할 수 있는 개수
    n = len(nums)//2
    return min(n, kinds)