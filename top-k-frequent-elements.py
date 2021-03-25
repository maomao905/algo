"""
[1,1,1,2,2,3] k=2

m kinds of values m = 3 (1,2,3)

count hash map O(n)
count[1] = 3
count[2] = 2
count[3] = 1

valueでsortする O(mlogm)
in total, O(n + mlogm) -> worst O(nlogn)
better than nlogn -> n, klogk, mlogm

k fixed size list 

increment count map
count[1] = 4
count[2] = 3
count[3] = 3

k size min-heap (k = 2)
min-heap has 1,2
count[3] = 4
compare min=3 and current=4
remove min element(2) and push current element(3)
time: O(n) for count map + O(nlogk) for min-heap operations
in total, time O(nlogk), space O(n)
"""
from typing import List
from collections import Counter

# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
#         # heap = heapq.heapify(reverse_counter)
#         return heapq.nlargest(k, counter, key=counter.get)

"""
bucket sort (time: O(n), space: O(n))
- counter mapを作成 O(n)
- frequencyごとにbucketを作り、bucket sortして、最初のk番目までのbucketが答えになる O(n)
"""
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
# 
#         buckets = [[] for _ in range(len(nums))]
# 
#         for num, freq in counter.items():
#             buckets[freq-1].append(num)
#         flatten_list = [el for bucket in buckets for el in bucket]
#         return flatten_list[-k:]

"""
quick select

"""
            

s = Solution()
print(s.topKFrequent([3,0,1,0], 1))
# print(s.topKFrequent([1], 1))
            
