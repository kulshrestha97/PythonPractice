from itertools import product
a, n = map(int,raw_input().split())
l = []

def su(number):
    return sum(x*x for x in number)

for i in range(0,a):
    s = map(int,raw_input().split())
    l.append((s[1:]))
combinations = list(product(*l))

print max(list(map(su, combinations)))



