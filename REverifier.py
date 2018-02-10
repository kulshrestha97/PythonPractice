import re
# def re_verify(i):

n = int(raw_input())
for _ in range(n):
    i = raw_input()
    try:
        re.compile(i)
        print "True"
    except:
        print "False"
