def birthdayCakeCandles(n,ar):
    ar.sort()
    s = 0
    for i in ar:
        if(i==ar[n-1]):
            s+=1
    return s

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))

result = birthdayCakeCandles(n, ar)
print(result)
