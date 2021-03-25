import heapq

class KthLargestNumberInStream:
    # O(NlogN)
    # space: O(K)
    def __init__(self, nums, k):
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k = k
        while len(self.min_heap) > self.k:
            # O(logN)
            heapq.heappop(self.min_heap)
    
    # O(logK)
    def add(self, num):
        if self.min_heap[0] < num:
            heapq.heapreplace(self.min_heap, num)
        return self.min_heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
