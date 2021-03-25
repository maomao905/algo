"""
use hash set to check if the element is in the array
we can use index itself as a value because 
next greater nonnegative integer is always O <= x <= x

time: O(N), space: O(N)
"""

def get_different_number(arr):
    seen = set(arr)
    N=len(arr)
    for i in range(N):
        if i not in seen:
            return i
    return N

"""
in-place modification
swap the value with the value's index

[2,3,5]
[5,3,2]

[1,2,3]
[3,1,2]

[2,3,0,1] -> [0,3,2,1] -> [0,1,2,3]

[0,5,4,1,3,6,2]
[0,6,4,1,3,5,2]
[0,2,4,1,3,5,6]
[0,4,2,1,3,5,6]
[0,3,2,1,4,5,6]
[0,1,2,3,4,5,6]

we cannot do like this because arr[i] is already changed before swapping
arr[i], arr[arr[i]] = arr[arr[i]], arr[i]

time: O(N) space: O(1)
"""
def get_different_number(arr):
    N=len(arr)
    for i in range(N):
        val = arr[i]
        while arr[i] < N and val != i:
            arr[i], arr[val] = arr[val], arr[i]
            val = arr[i]
    
    for i in range(N):
        if i != arr[i]:
            return i
    return N

# print(get_different_number([2,3,5]))
# print(get_different_number([0,1,2,3]))
print(get_different_number([1,0,2,3]))
print(get_different_number([0,5,4,1,3,6,2]))
