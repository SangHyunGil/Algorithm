# 아스키 코드를 활용한 코드
def solution(numbers):
    for num in numbers:
        if ord('0') <= ord(num) <= ord('9'):
            continue
            
        return False
        
    return True if len(numbers) in (4, 6) else False


# isdigit()를 활용한 코드
# def solution(numbers):
#     return numbers.isdigit() and len(numbers) in (4, 6)