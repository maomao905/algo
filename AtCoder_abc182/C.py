from itertools import combinations
# inputs=list(input())
inputs=list(map(int, list(input())))
# inputs = [int(_str) for _str in _inputs if int(_str) % 3 != 0]

# print(inputs)
N = len(inputs)
for size in range(N):
    for comb in combinations(inputs, N-size):
        if sum(comb) % 3 == 0:
            print(size)
            exit()
print(-1)
