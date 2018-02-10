a = raw_input().split(' ')
a = [int(i) for i in a]
n = a[0]
m = a[1]
happy = 0
arr = [int(i) for i in raw_input().split(' ')]
if (n == len(arr)):
    True
else:
    exit()
setA = set([int(i) for i in raw_input().split(' ')])
setB = set([int(i) for i in raw_input().split(' ')])
if (len(setA)==len(setB)):
    True
else:
    exit()
for i in arr:
    for j in setA:
        if i == j:
            happy+=1
        else:
            happy+=0
for i in arr:
    for k in setB:
        if i == k:
            happy+= -1
        else:
            happy+=0

print happy
'''
     My Code was right, but it was not efficient, hence occured the
     time inefficiency, which made me realise that I should study
     DSA for python. As I am taking Python as my first lang.
'''