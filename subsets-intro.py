"""
BFS
- 既存のものを再度取り出して、既存のものに追加したものを追加していく
time: O(2^N) * O(N) for list copy
space: O(N*2^N)
"""

def find_subsets(nums):
  subsets = []
  
  subsets.append([])
  for i in range(len(nums)):
      # print(len(subsets))
      for j in range(len(subsets)):
          subset = list(subsets[j]) # copy
          subset.append(nums[i])
          subsets.append(subset)
  
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
