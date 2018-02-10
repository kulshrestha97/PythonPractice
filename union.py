m = input()
s1 = set(map(int, raw_input().split()))
n = input()
s2 = set(map(int, raw_input().split()))
s3 = s1.union(s2)
print len(s3)
print "--END OF UNION CODE--"

# for intersection

m = input()
s1 = set(map(int, raw_input().split()))
n = input()
s2 = set(map(int, raw_input().split()))
s3 = s1.intersection(s2)
print len(s3)
print "--END OF INTERSECTION CODE--"
