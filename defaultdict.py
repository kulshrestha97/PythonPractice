from collections import defaultdict
d = defaultdict(list)
n, m = map(int,raw_input().split())
first = []
for i in range(0,m+n):
    first.append(raw_input())
print first[n:(m+n)]
print first[0:n]
for k in first[n:(m+n)]:
    for i,j in enumerate(first):
        if(k==j):
            d[j].append(i+1)
        elif len(set(first[n:(m+n)])-set(first[0:n]))!= 0:

            d[str(set(first[n:(n+m)])-set(first[0:n]))].append(-1)

print len(set(first[n:(m+n)])-set(first[0:n]))

for j in d.values():
    print " ".join(set(map(str,j)))
