"""
brute-force
all combinations
sum/2 is the goal
time: O(2^N)
space: O(N)

memorization
indexとremain_sumをkeyにしてmemorizeする
time: O(N*sum)
space: O(N*sum)
"""
def can_partition(nums):
  def recursive(remain_sum, i):
      if remain_sum == 0:
          return True
      
      if i >= len(nums):
          return False
      
      if not dp[i][remain_sum]:
          # include current index
          _remain_sum = remain_sum - nums[i]
          if _remain_sum >= 0:
              if recursive(_remain_sum, i+1):
                  dp[i][remain_sum] = True
                  return True
          # exclude current index
          dp[i][remain_sum] = recursive(remain_sum, i+1)
      return dp[i][remain_sum]
         
  if sum(nums) % 2 == 1:
      return False
  subset_sum = sum(nums) // 2
  
  dp = [[False] * (subset_sum+1) for _ in range(len(nums))]
  
  return recursive(subset_sum, 0)
  

"""
bottom-up fashion
dp[i][s]
0 <= i < len(nums)
0 <= s <= 2/sum
time and space O(N*S)
"""
def can_partition(nums):
    S = sum(nums)
    if S % 2 == 1:
        return False
    
    dp = [[False] * (S//2) for _ in range(len(nums))]
    
    for i, n in enumerate(nums):
        for s in range(1, (S//2)+1):
            if n == s:
                dp[i][s-1] = True
            # num=2, sum=3
            if s < n:
                # 一つ上のrowを見る
                if dp[i-1][s-1]:
                    dp[i][s-1] = True
            # num=3, sum=4
            else:
                # 一つ上の行で、現在のnumを引いた残りのsum(4-3)がTrueであればTrue
                if i-1 >= 0 and dp[i-1][s-n-1]:
                    dp[i][s-1] = True
            
    return dp[-1][-1]
                
                
    

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))
  # print("Can partition: " + str(can_partition([2, 4, 6, 8, 12])))
  # print("Can partition: " + str(can_partition([1, 2, 3, 4, 5, 6, 7])))


main()
