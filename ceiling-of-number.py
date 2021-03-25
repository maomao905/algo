"""
sorted and find the position -> binary search
[1,2,3] 0 -> index 0 つまり最小の値(1)よりも小さい場合は、最小の値が答えになる
[1,2,3] 4 -> index -1 最大を超えた場合は-1

time: O(logN)
space: O(1)
"""
def search_ceiling_of_a_number(arr, key):
  left, right = 0, len(arr)-1
  
  if key > arr[right]:
      return -1
  
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] == key:
          return mid
      
      if key < arr[mid]:
          right = mid - 1
      else:
          left = mid + 1
  
  # 値が見つからなかったとしても、それより一つ前の値のindex(left)を返せば良い
  return left

def search_floor_of_a_number(arr, key):
  left, right = 0, len(arr)-1
  
  if key < arr[left]:
      return -1
  
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] == key:
          return mid
      
      if key < arr[mid]:
          right = mid - 1
      else:
          left = mid + 1
  
  # 値が見つからなかったとしても、それより一つ前の値のindex(right)を返せば良い
  return right


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))
  print(search_floor_of_a_number([4, 6, 10], 6))
  print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_floor_of_a_number([4, 6, 10], 17))
  print(search_floor_of_a_number([4, 6, 10], -1))


main()
