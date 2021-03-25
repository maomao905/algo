from random import randint

def partition(l, r, pivot):
    i = l
    # move pivot to the end
    arr[pivot], arr[r] = arr[r], arr[pivot]
    pivot = r
    # move smaller elements to the left
    # move greater elements to the right
    for j in range(l, r):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # place pivot to the right index
    arr[r], arr[i] = arr[i], arr[r]
    return i
    
def kth_smallest(l, r, k):
    if l == r:
        return arr[l]
    pivot = randint(l,r)
    pivot = partition(l, r, pivot)
    if pivot == k:
        return arr[pivot]
    elif k < pivot:
        # go left
        return kth_smallest(l, pivot-1, k)
    else:
        # go right
        return kth_smallest(pivot+1, r, k)


from random import shuffle
arr = list(range(10))
shuffle(arr)
assert kth_smallest(0, len(arr)-1, 5) == 5
assert kth_smallest(0, len(arr)-1, 7) == 7
assert kth_smallest(0, len(arr)-1, 8) == 8
        
