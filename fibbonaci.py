cube = lambda i: pow(i,3)
def fibonacci(n):
    flist = [0,1]
    for i in range(2,n):
        flist.append(flist[i-1] + flist[i-2])
    return flist[0:n]
n = int(raw_input())
print map(cube,fibonacci(n))