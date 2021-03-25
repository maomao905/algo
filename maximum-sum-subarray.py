"""
time: O(N)
space: O(1)
k=3
0,1,2,3
"""
def max_sub_array_of_size_k(k, arr):
  window_sum, max_sum = 0, 0
  window_start = 0
  for window_end in range(len(arr)):
      window_sum += arr[window_end]
      if window_end >= k:
          window_sum -= arr[window_start]
          max_sum = max(max_sum, window_sum)
          window_start += 1
  return max_sum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
