n = int(input())
no = set(map(int, raw_input().split()))
s = int(input())

for i in range(0, s):
    statement = raw_input().split()
    if (statement[0] == 'intersection_update'):
        A = set(map(int, raw_input().split()))
        no.intersection_update(A)
    elif(statement[0] == 'update'):
        A = set(map(int, raw_input().split()))
        no.update(A)
    elif(statement[0] == 'symmetric_difference_update'):
        A = set(map(int, raw_input().split()))
        no.symmetric_difference_update(A)
    elif(statement[0] == 'difference_update'):
        A = set(map(int, raw_input().split()))
        no.difference_update(A)
print sum(no)

