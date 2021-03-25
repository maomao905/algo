"""
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
5,7,5,6,4,7
people[i] = [h_i, k_i]
h_i: height
k_i: k other people in front who have a greater height

taller person can ignore the smaller people
[5,2] -> they don't count the people who have a height of less than 5, but only taller people

time: O(N^2) space: O(1)
"""

from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        
        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res
            
s = Solution()
print(s.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
