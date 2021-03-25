N=int(input())
total = 0

def cal(n):
    return n * (n+1)

for _ in range(N):
    inputs = list(map(int, input().split()))
    total += (cal(inputs[1]) - cal(inputs[0]-1))/2
    

print(int(total))
    
