n = input()
s = set(map(int, raw_input().split()))
m = input()
for i in range(0, m):
    command = raw_input().split()

    if(command[0] == "pop"):
        s.pop()

    if(command[0] == "remove"):
        s.remove(int(command[1]))

    if(command[0] == "discard"):
        s.discard(int(command[1]))

print sum(s)
