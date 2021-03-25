class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(ni, depth):
            if ni.isInteger:
                return ni.getInteger * depth
            
            return sum(dfs(_ni, depth+1) for _ni in ni.getList())
            
        return dfs(nestedList, 0)
