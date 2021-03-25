def solve(nums):
    N = len(nums) + 1
    
    nums_xor = 0
    for num in nums:
        nums_xor ^= num
    
    n_xor = 0
    for n in range(1,N+1):
        n_xor ^= n
    
    return nums_xor ^ n_xor

print(solve([1, 5, 2, 6, 4]))
        
