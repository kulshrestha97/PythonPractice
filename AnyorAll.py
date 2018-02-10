
def palindrome(a):
    x = str(a)
    y = map(str,x)
    l = []
    for i in xrange(len(y),0,-1):
        l.append(y[i-1])
    if(l==y):
        return True
    else:
        return False



x = int(raw_input())
l = map(int,raw_input().split())
if(all(i>0 for i in l)):

    if(any(palindrome(i) for i in l)):
        print "True"
    else:
        print "False"

else:
    print "False"