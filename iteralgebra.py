from itertools import permutations
n = int(raw_input())
lowerlist = map(str,raw_input().split())
k = int(raw_input())
s=0
finallist = []
count = 0
for i in permutations(lowerlist,k):
    a = ''.join(map(str,i))
    finallist.append(a)
    if(a.find('a')>-1):
        s+=1
prob = (float(s)/float(len(finallist)))
print prob