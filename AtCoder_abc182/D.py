N=input()
inputs=list(map(int, input().split()))
# N=3
# inputs=[5
# -2 1 3 -1 -1]


max_score = 0
score = 0
max_add = 0
add = 0
# print(inputs)
for i in inputs:
    temp_score = score + max_add
    max_score = max(max_score, temp_score)
    add += i
    score += add
    max_score = max(max_score, score)
    # print(temp_score, score, max_score)
    max_add = max(max_add, add)
print(max_score)
