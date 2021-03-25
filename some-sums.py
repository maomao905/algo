N,A,B = map(int, input().split())

total = 0
for n in range(1,N+1):
    _n = n
    sum = 0
    while _n > 0:
        sum += _n%10
        _n = _n//10
    
    if A <= sum <= B:
        total += n

print(total)
