r=range
d={(i,j):1 for i in r(7)for j in r(i,7)}
s=0
m=[[*map(int,input())]for i in r(8)]
v=[[1]*7 for i in r(8)]
k=[[0]*7 for i in r(8)]
s=0
g=lambda i,j:tuple(sorted((i,j)))
t=set()
print(d)
def f(n):
    if n==28:global s;s+=1;return
    for i in r(8):
        for j in r(7):
            if v[i][j]:
                v[i][j]=0
                if j<6 and v[i][j+1] and d[(k:=g(m[i][j],m[i][j+1]))]:
                    d[k]=0
                    v[i][j+1]=0
                    f(n+1)
                    d[k]=1
                    v[i][j+1]=1
                if i<7 and v[i+1][j] and d[(k:=g(m[i][j],m[i+1][j]))]:
                    d[k]=0
                    v[i+1][j]=0
                    f(n+1)
                    d[k]=1
                    v[i+1][j]=1

                v[i][j]=1
                return
f(0)
print(s)