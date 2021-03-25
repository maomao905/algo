"""
edges = [[0,1], [1,2],[3,4]]
brute-force O(N^2)
1. 0-1 0 or 1を含むnodeを探す O(N)
2. if found, merge them O(1) [min, max]
3. 全ノードに対して繰り返す O(N)

Union-Find
"""

union_find = __import__('union-find')

# from union-find import UnionFind

# class Solution(object):
#     def countComponents(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: int
#         """
#         nodes = [i for i in range(n)]
# 
#         for edge in edges:
#             # [0, 1] 1's parent is 0
#             nodes[edge[1]] = edge[0]
# 
#         print(nodes)
# 
#         return len([i for i, node in enumerate(nodes) if node == i])

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = union_find.UnionFind(n)
        
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return len(uf.list_roots())
        
        
s = Solution()
print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(s.countComponents(3, [[1,0], [2,0]]))
