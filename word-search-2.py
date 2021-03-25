"""
build trie
O(WL) W: words.length L: words[i].length

search
O((3**L)*MN)

worst case
(3**10)*(12**2) = 8503056
"""
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie():
            trie = {}
            for w in words:
                node = trie
                for c in w:
                    if c not in node:
                        node[c] = {}
                    node = node[c]
                node['*'] = w
            return trie
        
        def dfs(i,j,node):
            char = board[i][j]
            hits = []
            if char not in node:
                return hits
            
            node = node[char]
            if '*' in node:
                hits.append(node['*'])
            
            # mark as visited
            board[i][j] = '-'
            for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                _i,_j = i+di,j+dj
                if 0<=_i<M and 0<=_j<N:
                    hits.extend(dfs(_i,_j,node))
            
            board[i][j] = char
            return hits
        
        M,N=len(board),len(board[0])
        
        trie = build_trie()
        res = set()
        for i in range(M):
            for j in range(N):
                res.update(dfs(i,j,trie))
        
        return list(res)

s = Solution()
print(s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
print(s.findWords([['a','b'],['c','d']], ['abcd']))
print(s.findWords([['a','a'],['a','d']], ['aaa']))
print(s.findWords([['a']], ['a']))
