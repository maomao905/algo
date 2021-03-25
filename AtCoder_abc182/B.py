N=input()
inputs=list(map(int, input().split()))

max_cnt = 0
max_input = 0
for i in range(2, min(max(inputs)+1, 1001)):
    current_cnt = len([_input for _input in inputs if _input % i == 0])
    if current_cnt > max_cnt:
        max_input = i
        max_cnt = current_cnt
    
    if max_cnt == len(inputs):
        print(max_input)
        exit()

if max_cnt == 1 and max_input in inputs:
    print(0)
else:
    print(max_input)
