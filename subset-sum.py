"""
1. brute-force
try all combinations
    - choose the current element or not
time: O(2^N)
space: O(N)

2. memorization
hash key is remain_sum and index
time: O(N*S)
space: O(N*S)
"""

def can_partition(nums, sum):
  def recursive(remain_sum, i):
      if remain_sum == 0:
          return True
      if len(nums) <= i or remain_sum < 0:
          return False
      
      if not dp[i][remain_sum]:
          # when include the current index
          if recursive(remain_sum-nums[i], i+1):
              dp[i][remain_sum] = True
              return True
          # when not include the current index
          dp[i][remain_sum] = recursive(remain_sum, i+1)
      return dp[i][remain_sum]
  
  dp = [[False] * (sum+1) for _ in range(len(nums))]
  return recursive(sum, 0)

"""
bottom-up dynamic programming
time and space: O(N*S)
"""
def can_partition(nums, sum):
    dp = [[False]*(sum+1) for _ in range(len(nums))]
    
    for i in range(len(nums)):
        num = nums[i]
        for _sum in range(sum+1):
            # sum=0は何も選ばなければ良いのでTrue
            if i == 0 and (_sum == 0 or num == _sum):
                dp[i][_sum] = True
                continue
            
            if dp[i-1][_sum]:
                dp[i][_sum] = True
            elif num <= _sum:
                # 一つ上の行の残りのsumがTrueかで判定
                dp[i][_sum] = dp[i-1][_sum-num]
    
    return dp[-1][-1]
"""
further improve bottom-up dynamic programming
we only need the previous row
if we traverse from the end, we can access the previous row in a single row
space: O(S)
"""
def can_partition(nums, sum):
    dp = [False]*(sum+1)
    
    for i in range(len(nums)):
        num = nums[i]
        for _sum in reversed(range(sum+1)):
            # sum=0は何も選ばなければ良いのでTrue
            if i == 0:
                if _sum == 0 or num == _sum:
                    dp[_sum] = True
                continue
            
            if not dp[_sum] and num <= _sum:
                # 一つ上の行の残りのsumがTrueかで判定
                dp[_sum] = dp[_sum-num]
    
    return dp[-1]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
