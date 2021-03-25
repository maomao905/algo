"""
duplicateがある場合は、一つ手前のstepで追加したものだけをcopyする
time and space: O(N * 2^N)
"""
def find_subsets(nums):
  subsets = []
  subsets.append([])
  
  start_index, end_index = 0, 0
  
  for i, n in enumerate(nums):
      end_index = len(subsets) - 1
      for j in range(start_index, end_index+1):
          new_subset = list(subsets[j])
          new_subset.append(n)
          subsets.append(new_subset)
      
      if i < len(nums)-1 and nums[i+1] == nums[i]:
          start_index = end_index + 1
      else:
          start_index = 0
          
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
