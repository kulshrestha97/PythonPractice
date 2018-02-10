from itertools import product
A = list(map(int, raw_input().split()))
B = list(map(int, raw_input().split()))
C = tuple(product(A,B))
D = map(str, C)
print ' '.join(i for i in D)
