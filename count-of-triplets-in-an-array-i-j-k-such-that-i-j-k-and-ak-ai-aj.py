"""
https://www.geeksforgeeks.org/count-of-triplets-in-an-array-i-j-k-such-that-i-j-k-and-ak-ai-aj/

i < j < k
a[k] < a[i] < a[j]

[2,5,1,3,0]
i j k
2,5,1
2,5,0
2,3,0
1,3,0


brute-force
O(N^3)

for i in range(N):
    for j in range(i, N):
        bigger than arr[i] [i, N]
        for k in range(j, N):
            smaller than arr[i] [j, N]
            (i, j, k)

O(N^2)
for i in range(N):
    for j in range(i, N):
        if bigger than arr[i] -> arr[j]
        if smaller than arr[i] -> arr[k]

"""

def solve(arr):
    N = len(arr)
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[j] > arr[i]:
                cnt += 1
            else:
                # if arr[j] < arr[i] -> we can consider j is k
                ans += cnt
    return ans

print(solve([2,5,1,3,0]))
            
    
