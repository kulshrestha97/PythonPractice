from itertools import combinations_with_replacement

string, n = raw_input().split()
no = int(n)
for i in combinations_with_replacement(sorted(string),no):
    print ''.join(i)


