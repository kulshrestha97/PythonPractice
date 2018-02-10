N, M = map(int, raw_input().split())
rows = [raw_input() for _ in range(N)]
K = int(raw_input())
print sorted(rows, key=lambda row: int(row.split()[K]))
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row.split()[K])