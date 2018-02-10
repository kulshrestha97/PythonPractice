s = raw_input()
slist=list(s)
lshow=[]

for i in slist:
    lshow.append([i.isalnum(),i.isalpha(),i.isdigit(),i.islower(),i.isupper()])


alnum=list()
alpha=list()
digit=list()
lower=list()
upper=list()
for i in range (0,len(s)):
    alnum.append(lshow[i][0])

for i in range (0,len(s)):
    alpha.append(lshow[i][1])

for i in range (0,len(s)):
    digit.append(lshow[i][2])

for i in range (0,len(s)):
    lower.append(lshow[i][3])

for i in range (0,len(s)):
    upper.append(lshow[i][4])


alnumA=False
digitA=False
lowerA=False
alphaA=False
upperA=False
for i in range(0,len(s)):
    alnumA=alnumA | alnum[i]

for i in range(0,len(s)):
    digitA=digitA | digit[i]

for i in range(0,len(s)):
    lowerA=lowerA | lower[i]

for i in range(0,len(s)):
    alphaA=alphaA | alpha[i]

for i in range(0,len(s)):
    upperA=upperA | upper[i]

finalAnswer=[alnumA,alphaA,digitA,lowerA,upperA]

for i in range(0,len(finalAnswer)):
    print finalAnswer[i]



