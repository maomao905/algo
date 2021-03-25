"""
5    0b00000101
25   0b00011001
5^25 0b00011100

more pairs of 0 and 1, XOR increases
-> check in each bit if there is an opposite bit
e.g.) 0b11001 -> find if 0b00110

bitwise trie
time: O(N*32) = O(N)
space: O(N)
"""


from typing import List
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # max length of binary form
        L = len(bin(max(nums)))-2
        
        # zero padding
        bin_nums = []
        for n in nums:
            bin_n = []
            for i in reversed(range(L)):
                # get ith bit
                bin_n.append((n >> i) & 1)
            bin_nums.append(bin_n)
        
        # build trie
        trie = {}
        for bin_n in bin_nums:
            node = trie
            for bit in bin_n:
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        max_xor = 0
        # find maximum xor
        for bin_n in bin_nums:
            node = trie
            xor = 0
            for i in range(len(bin_n)):
                bit = bin_n[i]
                # flip the bit
                flip_bit = bit ^ 1
                if flip_bit in node:
                    xor <<= 1
                    xor += 1
                    node = node[flip_bit]
                else:
                    node = node[bit]
                    xor <<= 1
            max_xor = max(max_xor, xor)
                
        return max_xor
        
s = Solution()
print(s.findMaximumXOR([3,10,5,25,2,8]))
print(s.findMaximumXOR([0]))
print(s.findMaximumXOR([2,4]))
print(s.findMaximumXOR([8,10,2]))
