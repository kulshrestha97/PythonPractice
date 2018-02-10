def rev(s):
    return s[::-1]

def isPalindrome(s):
    r = rev(s)
    if (s == r):
        if(len(s)%2 == 0):
            print "YES EVEN"
        elif(len(s)%2 != 0):
            print "YES ODD"
    else:
        print "NO"

t = int(raw_input())
for i in range(0,t):
    s = raw_input()
    isPalindrome(s)