"""
단순 문자열을 뒤집어 비교하면 된다.
"""
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        y = x[::-1]
        return x == y