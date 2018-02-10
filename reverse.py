def palindrome(s):
    a = 0
    print len(s)
    for i in(0,len(s)):
        if ((s[i] != s[len(s)-1-i])):
            a+=1;
    if(a>0):
        print "NO"
    elif(a==0):
        if(len(s)%2 == 0):
            print "YES EVEN"
        else:
            print "YES ODD"

a = int(raw_input())
for i in range(0,a):
    s = list(map(str,raw_input()))
    palindrome(s)