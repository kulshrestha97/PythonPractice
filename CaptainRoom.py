from collections import *
n = int(input())
s = list(map(int, input().split()))
count = Counter(s)
for value,occ in count.iteritems():

    if occ!= 1:
        continue
    else:
        print(value)
