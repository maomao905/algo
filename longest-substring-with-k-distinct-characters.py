"""
time: O(N)
space: O(K)
sliding window
use hash map to save the distinct chars and frequency
"""
from collections import Counter
def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  counter = Counter()
  for window_end in range(len(str)):
      counter[str[window_end]] += 1
      while len(counter) > k:
          counter[str[window_start]] -= 1
          if counter[str[window_start]] == 0:
              del counter[str[window_start]]
          window_start += 1
      max_length = max(max_length, window_end-window_start+1)
  return max_length

print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("araaci", 1))
print(longest_substring_with_k_distinct("cbbebi", 3))
