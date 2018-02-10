A = list(map(int, raw_input().split()))
B = list(map(int, raw_input().split()))
alicepoint = 0
bobpoint = 0

for i in range(0,len(A)):
    if(A[i]> B[i]):
        alicepoint+=1
    elif(A[i]<B[i]):
        bobpoint+=1

print alicepoint, bobpoint
