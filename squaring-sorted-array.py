def make_squares(arr):
  squares = [0] * len(arr)
  
  left, right = 0, len(arr)-1
  
  high_index = len(arr)-1
  
  while left < right:
      l, r = arr[left] ** 2, arr[right] ** 2
      if l > r:
          squares[high_index] = l
          left += 1
      else:
          squares[high_index] = r
          right -= 1
      
      high_index -= 1
      
  return squares

print(make_squares([-2, -1, 0, 2, 3]))
