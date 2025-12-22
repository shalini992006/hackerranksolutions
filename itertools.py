from itertools import product
A = list(map(int,input().split()))
B = list(map(int, input().split()))
for t in product(A, B):
    print(t, end=' ')