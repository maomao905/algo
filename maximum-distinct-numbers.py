import heapq
from collections import Counter
"""
time: O(N) + O(NlogN) -> O(NlogN)
space: O(N)
"""
def find_maximum_distinct_elements(nums, k):
    counter = Counter(nums)
    distinct_counts = 0
    heap = []
    for n, freq in counter.items():
        if freq == 1:
            distinct_counts += 1
        else:
            heapq.heappush(heap, (freq, n))
            
            
    for _ in range(k):
        if len(heap) > 0:
            freq, n = heapq.heappop(heap)
            freq -= 1
            if freq == 1:
                distinct_counts += 1
            else:
                heapq.heappush(heap, (freq, n))
        else:
            distinct_counts -= 1
    
    return distinct_counts


def main():
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
