"""
Trie

W: number of words
L: length of word
S: length of given target word
time: build trie O(WL) and search O(S^2) in worst
"""
from typing import List

class Node:
    def __init__(self, char, is_end):
        self.char = char
        self.is_end = is_end
        self.children = []
    
    def has_next_char(self, char):
        for node in self.children:
            if char == node.char:
                return True
        return False
    
    def get_child(self, char):
        for node in self.children:
            if char == node.char:
                return node
        return None
    
    def add_child(self, node):
        self.children.append(node)
    
    def set_end(self):
        self.is_end = True
    
    def __repr__(self):
        return f'char={self.char} end={self.is_end}'
    

def _print_all_children(node, i=0):
    print(f'level={i} char={node.char} end={node.is_end}')
    for child in node.children:
        _print_all_children(child, i+1)

from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node('', False)
        
        for word in wordDict:
            parent = root
            for i in range(len(word)):
                is_end = i == len(word)-1
                child = parent.get_child(word[i])
                if child is None:
                    child = Node(word[i], is_end)
                    parent.add_child(child)
                else:
                    if is_end:
                        child.set_end()
                parent = child
        q = deque([(0, root)])
        
        visited = set()
        cnt = 0
        while len(q) > 0:
            cnt += 1
            i, node = q.popleft()
            if node.is_end:
                # last character
                if i >= len(s):
                    print(cnt)
                    return True
                else:
                    if i not in visited:
                        q.append((i, root))
                        visited.add(i)
            if i >= len(s):
                continue
            child = node.get_child(s[i])
            # no word in dictionary
            if child is None:
                continue
            
            q.append((i+1, child))
        return False
                
"""
DP bottom-up

0th <------> jth <-----> ith
characters up to ith is made of characters up to jth + characters between jth and ith

time O(N^3) N^2 loop and N substring generation
space O(N)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dictionary:
                    dp[i] = True
                    break
        return dp[-1]
"""
recursive top-down with memorization
end -> [0, end] = [0,end-1] + [end-1,end]
       [0, end-1] = [0, end-2] + [end-2, end]
time: O(N^3)
space: O(N) depth of recursion is N
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursive(i, j):
            if (i,j) in ht:
                return ht[(i,j)]
            if s[i:j] in dictionary:
                return True
            
            for k in range(i, j):
                result = recursive(i, k) and recursive(k, j)
                ht[(i,j)] = result
                if result:
                    return True
            return False
        
        ht = {}
        dictionary = set(wordDict)
        return recursive(0, len(s))

s = Solution()
# print(s.wordBreak('leetcode', ['leet', 'code']))
# print(s.wordBreak('aaaaaa', ['a', 'aa', 'aaa', 'aaaa']))
# print(s.wordBreak('ab', ['a','b']))
# print(s.wordBreak('applepenapple', ['apple', 'pen']))
# print(s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
# print(s.wordBreak("bb", ["a","b","bbb","bbbb"]))
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
 ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
