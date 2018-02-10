from collections import Counter
sizes = int(raw_input())
shoe_size = Counter([int(x) for x in raw_input().split()])
p= 0
n = int(raw_input())
print shoe_size
for i in range(n):
    s, price = [int(x) for x in raw_input().split()]
    shoe_size[s]-=1
    if (shoe_size[s]>=0):
        p+=price
print p

