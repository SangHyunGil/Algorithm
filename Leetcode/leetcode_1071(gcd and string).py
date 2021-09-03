def gcd(a, b):
        if b==0: return a
        else: return gcd(b, a%b)

class Solution(object):  
    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1: return ""
        if len(str1) < len(str2): str1, str2 = str2, str1
        g = gcd(len(str1), len(str2))
        temp = str1[:g]
        str2 = str2.replace(temp, "")
        if len(str2) == 0:
            return temp
        else:
            return ""