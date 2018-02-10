from collections import Counter

count1 = Counter()
count2 = Counter()
a = input()
b = input()
for i in str.lower(a):
    count1[i]+=1
for j in str.lower(b):
    count2[j]+=1

if(count1==count2):
    print('Anagram')
else:
    print('Not Anagram')
