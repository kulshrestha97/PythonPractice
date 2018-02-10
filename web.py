def sum(sequence):
    s=0

    for i in sequence:
        s+=i


    return s

seq = list(map(int,(raw_input().split())))
print seq
su = sum(seq)
print su
