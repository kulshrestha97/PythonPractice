a,b = map(int,raw_input().split())
l1 = []
for i in xrange(b):
    l = []
    l = (map(float,raw_input().split()))
    l1.append(l)

marks = zip(*l1)
for _ in marks:
    print sum(_)/len(_)



