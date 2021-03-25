"""
similar to lowest common ancestor problem
n-ary tree

but we don't know the root

it may be topological sort
hash map A: small -> large
hash map B: large -> [small regions]
if key in A does not have large region, it's root (earth)
using B, we find the small regions of root, continue this process until it does not have small regions

after constructing tree, DFS

-> no, we don't need to identify root
just getting the parent of region1 and keep in hash set
and get the parent of region2 until it matches in hash set

Quebec -> Canada -> NorthAmerica (using small_to_large)
NewYork -> US -> NorthAmerica

time and space: O(N)
"""
from typing import List
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        all_regions = set()
        # large_to_small = {}
        small_to_large = {}
        
        for reg in regions:
            for i in range(1, len(reg)):
                # large_to_small[large].append(reg[i])
                small_to_large[reg[i]] = reg[0]
        
        reg1_ancestors = set()
        while region1 in small_to_large:
            region1 = small_to_large[region1]
            reg1_ancestors.add(region1)
        
        while region2 not in reg1_ancestors:
            region2 = small_to_large[region2]
        
        return region2

s = Solution()
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
region1 = "Quebec"
region2 = "New York"
print(s.findSmallestRegion(regions, region1, region2))
                
