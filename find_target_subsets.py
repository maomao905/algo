"""
use all numbers
[1,1,2,3] S=1
output=3
    - -1+1-2+3
    - 1-1-2+3 -> (1+3) - (1+2) = 1 -> Sum(S1) - Sum(S2) = S
    - 1+1+2-3
Sum(S1) - Sum(S2) = S
Sum(s1) + Sum(s2) = Sum(nums)
Sum(s1) = (S + Sum(nums))/2 <-- こうなるようなs1をdpで求めれば良い
"""
def find_target_subsets(nums, s):
    s1 = (sum(nums) + s) // 2
    # print(s1)
    dp = [[0] * (s1+1) for _ in range(len(nums))]
    
    dp[0][0] = 1
    
    for i in range(len(nums)):
        n = nums[i]
        if i == 0:
            dp[i][n] = 1
            continue
        
        for _s in range(s1+1):
            if n > _s:
                dp[i][_s] = dp[i-1][_s]
            else:
                dp[i][_s] = dp[i-1][_s] + dp[i-1][_s-n]
    print(dp)
    return dp[-1][-1]

def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
