s = raw_input().strip()
count = 0
for i in s:
    if (ord(i)<97):
        count+=1
print count+1
