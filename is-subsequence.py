"""
two pointers
time: O(T)
space: O(1)

recursion
time: O(T)
space: O(T)

dynamic programming
time: O(ST)
space: O(ST) for dp table

hash map
time: O(T + SlogT)
    - build hash map O(T)
    - binary search S times for finding the index O(logT) in worst
space: O(T) for storing hash map
"""
class Solution:
    def isSubsequence(self, source: str, target: str) -> bool:
        if source == '':
            return True
        
        p_source = 0
        
        for t in target:
            if source[p_source] == t:
                p_source += 1
                
                if p_source == len(source):
                    return True
        
        return False

s = Solution()
print(s.isSubsequence('abc', 'ahbgdc'))
print(s.isSubsequence('axc', 'ahbgdc'))

            
        
