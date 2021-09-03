def gcd(a, b):
    if b==0: return a
    else: return gcd(b, a%b)

def gcdOfStrings(str1, str2):
    if len(str1) < len(str2): str1, str2 = str2, str1
    g = gcd(len(str1), len(str2))
    temp = str1[:g]
    print(str2, temp)
    print(temp == str2)
    str22 = str2.replace("ABC", "")
    print(str22)
    if len(str22) == 0:
        print(temp)
    else:
        print("")

print(gcdOfStrings("ABCABC", "ABC"))