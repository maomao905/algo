"""
brute-force
try all combinations and choose the one with maximum value
time: O(2^n)
space: O(n) DFS search n recursive at most at any time

-> use memorization to solve overlapping subproblems
time: O(N*C)
space: O(N*C)
"""
def solve_knapsack(profits, weights, capacity):
    # return recursive_knapsack(profits, weights, capacity)
    return bottom_up_recursive_improved2(profits, weights, capacity)

def recursive_knapsack(profits, weights, capacity, index=0, memo={}):
    if index >= len(profits):
        return 0
    
    if (index, capacity) in memo:
        return memo[(index, capacity)]
    
    p1 = recursive_knapsack(profits, weights, capacity, index+1)
    
    p2 = 0
    if capacity - weights[index] >= 0:
        p2 = recursive_knapsack(profits, weights, capacity - weights[index], index+1) + profits[index]
    
    memo[(index, capacity)] = max(p1, p2)
    return memo[(index, capacity)]

"""
bottom up approach
time O(N*C), C: capacity size, N: num of products
space O(N*C)
"""
def bottom_up_recursive(profits, weights, capacity):
    if capacity <= 0:
        return 0
    dp = [[0] * (capacity+1) for _ in range(len(profits))]
    for index in range(len(profits)):
        for cap in range(capacity+1):
            # cap < weights[index] capacity overなので、現在のindexは追加できないので、一つ前のindexの同じcapacityのvalueを見る
            if cap < weights[index]:
                # index-1はないので、最初の0のprofitままでok
                if index == 0:
                    continue
                dp[index][cap] = dp[index-1][cap]
            else:
                if index == 0:
                    dp[index][cap] = profits[index]
                else:
                    # 現在のindexを追加しない or 追加する
                    dp[index][cap] = max(dp[index-1][cap], profits[index] + dp[index-1][cap-weights[index]])
    
    print(dp)
    return dp[len(dp)-1][len(dp[0])-1]

"""
we only need previous row, so index % 2 is applicable
space O(2C) = O(C)
"""
def bottom_up_recursive_improved(profits, weights, capacity):
    if capacity <= 0:
        return 0
    dp = [[0] * (capacity+1) for _ in range(2)]
    for index in range(len(profits)):
        for cap in range(capacity+1):
            # cap < weights[index] capacity overなので、現在のindexは追加できないので、一つ前のindexの同じcapacityのvalueを見る
            if cap < weights[index]:
                # index-1はないので、最初の0のprofitままでok
                if index == 0:
                    continue
                dp[index%2][cap] = dp[(index-1)%2][cap]
            else:
                if index == 0:
                    dp[index%2][cap] = profits[index]
                else:
                    # 現在のindexを追加しない or 追加する
                    dp[index%2][cap] = max(dp[(index-1)%2][cap], profits[index] + dp[(index-1)%2][cap-weights[index]])
    
    print(dp)
    return dp[(len(dp)-1)%2][len(dp[0])-1]

def bottom_up_recursive_improved2(profits, weights, capacity):
    if capacity <= 0:
        return 0
    dp = [0] * (capacity+1)
    for index in range(len(profits)):
        for cap in range(capacity, -1, -1):
            # cap < weights[index] capacity overなので、現在のindexは追加できないので、一つ前のindexの同じcapacityのvalueを見る
            if cap >= weights[index]:
                dp[cap] = max(dp[cap], profits[index] + dp[cap-weights[index]])
    
    return dp[-1]

"""
   cap  0  1  2  3   4   5   6 
p   w
1   1  [0, 1, 1, 1,  1,  1,  1],
6   2  [0, 1, 6, 7,  7,  7,  7],
10  3  [0, 1, 6, 10, 11, 16, 17]
...
"""

print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)) # 22
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)) # 17
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)) # 16
