import heapq
from collections import Counter

"""
time: O(DlogD) + O(N) for string concatnation -> O(NlogN)
D: distinct characters: worst case is all characters are unique O(NlogN)
"""

def sort_character_by_frequency(str):
  counter = Counter(str)
  min_heap = []
  
  for char, cnt in counter.items():
      heapq.heappush(min_heap, (-cnt, char))
  
  char_array = []
  while len(min_heap) > 0:
      cnt, char = heapq.heappop(min_heap)
      for _ in range(abs(cnt)):
          char_array.append(char)
      
  return ''.join(char_array)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
