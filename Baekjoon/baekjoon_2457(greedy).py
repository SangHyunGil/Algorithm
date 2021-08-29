alpha = []
for _ in range(26):
    alpha.append(0)

for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        alpha[ord(s[i])-ord('A')] += 10 ** (len(s)-i-1)

print(alpha) 
alpha.sort(reverse = True)

s = 0
for i in range(26):
    if(alpha[i] != 0):
        s = s + alpha[i] * (9 - i)
    else:
        break
        
print(s)