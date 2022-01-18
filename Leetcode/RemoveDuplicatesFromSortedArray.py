"""
중복되는 부분을 제거하는 문제이다.
유의해야되는 부분은 nums에 순차적으로 중복되지 않는 순으로 저장되고
그 뒤에는 어느 숫자가 와도 상관없다. (단순 앞 부분만 return 값을 이용해 체크한다.)
이러한 부분에 있어 다음과 같이 처리했다.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        for num in nums[1:]:
            if nums[idx] != num:
                idx += 1
                nums[idx] = num
                
        return idx+1
                