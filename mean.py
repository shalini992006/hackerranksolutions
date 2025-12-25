import numpy as np
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
a = np.array(arr)
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a), 11))
   