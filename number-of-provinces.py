class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in range(len(M)):
                if M[i][j] == 1:
                    dfs(j)
        
        cnt = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt
