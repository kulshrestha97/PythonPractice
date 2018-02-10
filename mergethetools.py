
string, k = raw_input(), int(raw_input())
n = len(string)
s = list(map(str,string))
b = []
c = []
v = str()
for i in range(0,n,k):
    b=list(set([s[j]for j in range(i, i+k)]))
    if (b not in c):
        c.append(b)
    print c

for i in c:
    for j in range(0,len(i)):
        v+=i[j]
    print v
    v=''
