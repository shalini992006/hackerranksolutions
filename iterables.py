from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
indices = list(range(n))
all_combinations = list(combinations(indices, k))
count = 0
for comb in all_combinations:
    if any(letters[i] == 'a' for i in comb):
        count += 1
probability = count / len(all_combinations)
print(f"{probability:.4f}")
