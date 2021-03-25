"""
time and space O(N*S)
"""
def count_subsets(nums, sum):
    # initialize dp table
    dp = [[0] * (sum + 1) for _ in range(len(nums))]
    
    dp[0][0] = 1
    
    for i in range(len(nums)):
        if i == 0:
            dp[i][nums[i]] = 1
            continue
        for s in range(sum+1):
            if nums[i] > s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] + dp[i-1][s-nums[i]]
    
    return dp[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
