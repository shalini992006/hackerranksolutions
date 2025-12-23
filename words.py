n = int(input())

count = {}
for _ in range(n):
    word = input().strip()

    count[word] = count.get(word, 0)+1
print(len(count))
for v in count.values():
    print(v, end=" ")