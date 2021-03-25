"""
first: divide half until only one element
second: merge them
"""

def mergeSort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2 # find the middle of the array
    # divide the array into 2 halves
    # 最小で2つになる
    L = arr[:mid]
    R = arr[mid:]
    print(L, R)
    
    mergeSort(L)
    mergeSort(R)
    
    i = j = 0 # two iterators for two halves
    k = 0 # iterator for the main list
    
    import pdb; pdb.set_trace()
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            # move the left iterator forward
            i += 1
        else:
            arr[k] = R[j]
            # move the right iterator forward
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    

# arr = [12, 11, 13, 5, 6, 7]
arr = [13, 12]
mergeSort(arr)
print(arr)

    
