"""
counter of s1

iterate s2
if match with one of s1, decrement counter
    continue it unitil counter is empty
    if it doesn't hit on half way, reset the counter
"""

from collections import Counter
from copy import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        L = len(s1)
        counter = Counter(s1)
        
        window_counter = Counter()
        first_hit = True
        
        for i in range(len(s2)):
            l = s2[i]
            window_counter[l] += 1
            
            if i < L-1:
                continue
            
            if window_counter == counter:
                return True
            start_l = s2[i-L+1]
            window_counter[start_l] -= 1
            if window_counter[start_l] == 0:
                del window_counter[start_l]
        
            
        return False

s = Solution()
print(s.checkInclusion('ab', 'eidbaooo'))
print(s.checkInclusion('ab', 'eidboaoo'))
print(s.checkInclusion('adc', 'dcda'))
print(s.checkInclusion('adc', 'dca'))
print(s.checkInclusion('adc', "ccccbbbbaaaa"))
                    
                
