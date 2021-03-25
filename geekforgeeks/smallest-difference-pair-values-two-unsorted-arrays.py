"""
two pointers
sort A, B

move pointers of smaller value

O(NlogN + MlogM + M + N) -> O(NlogN + MlogM)
"""

def solve(A, B):
    A.sort()
    B.sort()
    
    a = b = 0
    
    min_diff = float('inf')
    while a < len(A) and b < len(B):
        min_diff = min(abs(A[a]-B[b]), min_diff)
        
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    return min_diff

print(solve([1, 3, 15, 11, 2],[23, 127, 235, 19, 8]))
            
