N, X = map(int, input().split())
inputs = list(input())

for i in inputs:
    if i == 'o':
        X += 1
    else:
        X = max(X-1, 0)

print(X)
