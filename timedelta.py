
n = int(raw_input())
def fun(a,b):
    try:
        print int(a)/int(b)
    except ZeroDivisionError as e:
        print "Error Code:",e

    except ValueError as e:
        print "Error Code:",e

for i in range(n):
    x,y = map(str,raw_input().split())
    fun(x,y)


