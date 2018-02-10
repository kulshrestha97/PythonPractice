a = int(input())
inp1 = raw_input()
set1 = set(inp1.split(' '))

b = int(input())
inp2 = raw_input()
set2 = set(inp2.split(' '))
diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
finalset = diff1.union(diff2)
finallist = list(finalset)
answer = [int(i) for i in finallist]
answer = sorted(answer,key=int)

for i in answer:
    print i