# def smallest_subarray_with_given_sum(s, arr):
#   left, right = 0, 0
#   smallest_length = float('inf')
#   current_sum = arr[0]
#   while left < len(arr) and right < len(arr):
#       if current_sum < s:
#           right += 1
#           if right < len(arr):
#               current_sum += arr[right]
#       else:
#           # print(left, right, current_sum)
#           smallest_length = min(smallest_length, right-left+1)
#           if left < len(arr):
#               current_sum -= arr[left]
#           left += 1
#   if smallest_length == float('inf'):
#       return 0
#   else:
#       return smallest_length

def smallest_subarray_with_given_sum(s, arr):
  smallest_length = float('inf')
  window_start = 0
  window_sum = 0
  
  for window_end in range(len(arr)):
      window_sum += arr[window_end]
      while window_sum >= s:
          smallest_length = min(smallest_length, window_end - window_start + 1)
          # print(window_start, window_end, window_sum)
          window_sum -= arr[window_start]
          window_start += 1
  
  if smallest_length == float('inf'):
      return 0
  else:
      return smallest_length

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
print(smallest_subarray_with_given_sum(8, [3,4,1,1,6]))
