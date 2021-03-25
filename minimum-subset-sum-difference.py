def can_partition(nums):
    max_sum = sum(nums) // 2
     
    dp = [[False] * (max_sum+1) for _  in range(len(nums))]
    
    for i, n in enumerate(nums):
        for s in range(max_sum+1):
            # sum=0は必ず可能とする
            if s == 0:
                dp[i][s] = True
            
            if i == 0:
                if n == s:
                    dp[i][s] = True
            else:
                # use previous row result
                if s < n:
                    dp[i][s] = dp[i-1][s]
                else:
                    dp[i][s] = dp[i-1][s-n]
    
    max_subset_sum = 0
    # search last dp row for the max subset sum
    for s in range(max_sum, -1, -1):
        if dp[-1][s]:
            max_subset_sum = s
            break
            
    return abs(max_subset_sum - (sum(nums) - max_subset_sum))


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
