n = int(raw_input())
marks = []
newmarks = []
for i in xrange(0,n):
    m = int(raw_input())
    marks.append(m)
for i in marks:
    a = i//5
    multiple = (a+1)*5
    if ((multiple - i)<3 and i>=38):
        newmarks.append(multiple)
    else:
        newmarks.append(i)

print "\n".join(map(str,newmarks))