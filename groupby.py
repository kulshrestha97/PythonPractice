from itertools import groupby
string = raw_input()
a = []
b=str()
for i,j in groupby(string):
    a.append((sum(1 for _ in j),int(i)))
    a.append(' ')
print ''.join(map(str,a))
