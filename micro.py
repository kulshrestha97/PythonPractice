t = int(raw_input())
an = list()

for i in range(0,t):
    n, k = map(int, raw_input().split())
    l = map(int,raw_input().split())
    a = min(l)
    s = k-a
    if(s>0):
        an.append(s)
    elif(s<0):
        an.append(0)
for i in an:
    print i

