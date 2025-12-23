from collections import Counter
s = input().strip()
freq = Counter(s)
sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
for i in range(3):
    print(sorted_chars[i][0], sorted_chars[i][1])


