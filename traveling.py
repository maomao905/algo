"""
i: 1 <= N
N=2

t=3 (x,y) = (1,2)
t=6 (x,y) = (1,1)
"""
N=int(input())
t = x = y = 0
for _ in range(N):
    _t, _x, _y = map(int, input().split())
    t_diff = _t - t
    dist = abs(_x - x) + abs(_y - y)
    if t_diff < dist:
        print('No')
        exit()
    
    if dist % 2 == 0 != t_diff % 2:
        print('No')
        exit()
    
    t = _t
    x = _x
    y = _y

print('Yes')
