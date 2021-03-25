class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        N=len(preorder)
        i = 0
        def dfs():
            nonlocal i
            if i >= N:
                return False
            
            if preorder[i] == '#':
                return True
            
            for _ in range(2):
                i += 1
                if not dfs():
                    return False
            
            return True
        
        return dfs() and i == N-1

s = Solution()
print(s.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
print(s.isValidSerialization('1,#'))
print(s.isValidSerialization('9,#,#,1'))
