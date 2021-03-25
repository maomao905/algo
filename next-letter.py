"""
time: O(logN)
space: O(1)
"""

def search_next_letter(letters, key):
    nums = [ord(l) for l in letters]
    
    # make dummy for circular list
    nums.append(ord('z')+1)
    
    target = ord(key)
    
    # binary search
    
    left = 0
    right = len(nums)-1
    
    while left < right:
        mid = left + (right-left) // 2
        # print(left, right, mid, target < nums[mid])
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    
    # print(chr(nums[left]), chr(nums[right]))
    
    if nums[left] == target:
        left += 1
        
    if nums[left] >= ord('z'):
        return letters[0]
        
    return chr(nums[left])


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))

main()
