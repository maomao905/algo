"""
time: O(logN)
space: O(1)
"""

def binary_search(arr, key):
  left = 0
  right = len(arr) - 1
  
  is_ascending = True if arr[left] < arr[right] else False
  
  while left <= right:
      mid = (left + right) // 2
      # print(left, right, mid)
      if arr[mid] == key:
          return mid
      if is_ascending:
          if key < arr[mid]:
              right = mid-1
          else:
              left = mid+1
      else:
          if key > arr[mid]:
              right = mid-1
          else:
              left = mid+1

  return -1

def main():
  print(binary_search([4, 6, 10], 10)) # 2
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5)) # 4
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()
