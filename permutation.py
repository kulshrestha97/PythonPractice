from itertools import permutations
from itertools import combinations
inp = raw_input().split()

LIST = list((permutations(inp[0],int(inp[1]))))
LIST.sort()
a = str()

for i in range(0, len(LIST)):
    for j in range(0, int(inp[1])):
        a+=LIST[i][j]
    print a
    a = ''



