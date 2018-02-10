from prod import permutations
from time import *

arr = map(int,raw_input().strip().split(' '))
s = list()
a = set()
for i in permutations(arr,4):
    (s.append(sum(i)))
print min(set(s)), max(set(s))
a = "".join(map(str, arr))
print a