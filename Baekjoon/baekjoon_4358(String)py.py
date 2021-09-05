import sys
from collections import defaultdict
 
readline = sys.stdin.readline
 
def main():
    dic = defaultdict(int)
    tot = 0
    try:
        while 1:
            word = readline().rstrip()
            if not word:
                break
            dic[word] += 1
            tot += 1
    except EOFError:
        exit()
 
    for t in sorted(dic.keys()):
        print(t,format(dic[t]/tot*100,'.4f'))
if __name__=='__main__':
    main()
