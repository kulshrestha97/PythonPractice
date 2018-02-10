s,t = map(int,raw_input().split())
a,b = map(int,raw_input().split())
m,n = map(int,raw_input().split())
l1 = map(int,raw_input().split())
l2 = map(int,raw_input().split())
print (sum(1 for x in l1 if(x+a)>=s and (x+a)<=t))
print (sum(1 for x in l2 if(x+b)>=s and (x+b)<=t))


