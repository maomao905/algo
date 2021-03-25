"""
N=9枚
Y=15000円

10000円,5000円,1000円

10000*1 + 5000
          5000*1 + 0
          5000*0 + 5000
                   1000*5
10000*0 + 15000
          5000*3 + 0
          5000*2 + 5000
                   1000*5
          5000*1 + 10000
                   1000*10
          5000*0 + 15000
                   1000*15
                   
dynamic programming
    - recursion and memorization

1 <= N <= 2000
2000 ** 2 = 4000000
"""

N, Y=map(int, input().split())
# N, Y = 9, 45000





for x in range(N+1):
    for y in range(N-x+1):
        z = N - x - y
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()

print(-1,-1,-1)
