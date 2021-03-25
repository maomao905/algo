"""
time: O(N)
space: O(1)
"""

def remove_duplicates(arr):
    unique_pointer = 0
    
    for i in range(len(arr)):
        if arr[unique_pointer] != arr[i]:
            unique_pointer += 1
            arr[unique_pointer] = arr[i]
    return unique_pointer+1

def remove_duplicates_key(arr, k):
    unique_pointer = 0
    
    for i in range(len(arr)):
        if arr[i] == k:
            continue
        else:
            if i != unique_pointer:
                arr[unique_pointer] = arr[i]
            unique_pointer += 1
    
    return unique_pointer

def main():
    # print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    # print(remove_duplicates([2, 2, 2, 11]))
    print(remove_duplicates_key([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_duplicates_key([2], 3))


main()
