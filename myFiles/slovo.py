A = {}
for w in input().split():
    A[w] = A.get(w, 0)+1
print(A[w]-1, end='')
