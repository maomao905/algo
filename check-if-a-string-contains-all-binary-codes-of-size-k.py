"""
get all combinations of size k and store them in hash map

sliding window and use rolling hash to check if the substring exists in hash map

time O(2^K + O(N)) = O(2^N)

even we don't need to store combinations in hash map
but we only need the number of combinaions (2 ** k)

sliding window and store substring in hash map and if the size of hashmap == the number of combinaions, 
return true

clear leftmost bit and add new bit at the rightmost in every step

time O(N) space O(N)
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N=len(s)
        n = int(s[:k], 2)
        seen = set([n])
        for i in range(k,N):
            # clear kth bit
            n &= ~(1 << k-1)
            n <<= 1
            # set new bit
            n |= int(s[i])
            seen.add(n)
        
        return len(seen) == 1 << k

s = Solution()
print(s.hasAllCodes('00110110', 2))
print(s.hasAllCodes('00110', 2))
print(s.hasAllCodes('0110', 1))
print(s.hasAllCodes('0110', 2))
print(s.hasAllCodes('0000000001011100', 4))
