from prod import combinations
inp = raw_input().split()
a = str()
L = []
for i in range(1,int(inp[1])+1):
    for j in combinations(sorted(inp[0]),i):
        print ''.join(j)