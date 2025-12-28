from itertools import combinations
S, k = input().split()
k = int(k)
S = sorted(S)
for i in range(1, k + 1):
    for comb in combinations(S, i):
        print("".join(comb))