N=int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]

def cal(i):
    ht = set()
    x1, y1 = inputs[i][0], inputs[i][1]
    for j in range(i+1, N):
        x2, y2 = inputs[j][0], inputs[j][1]
        x_diff = x2-x1
        r = 'x=0' if x_diff == 0 else (y2-y1)/x_diff
        
        if r in ht:
            return True
        
        ht.add(r)

    return False

for _i in range(N):
    if cal(_i):
        print('Yes')
        exit()
print('No')
