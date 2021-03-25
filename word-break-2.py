"""
build trie and as long as there is a hit in trie, keep going

time: O(2^N) + O(WL)
O(WL) build trie W: length of word dict array, L: average length of word
O(2^N) because we have two choices in every step (it is the end char of dictionary or not)
"""
from typing import List
from collections import defaultdict
class Solution:
    def create_trie(self, words):
        trie = {}
        
        for w in words:
            cur = trie
            for char in w:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['*'] = None
        return trie
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.create_trie(wordDict)
        
        # check if s contains the character which is not in dictionary
        if set(s) > set(''.join(wordDict)):
            return []
        
        res = []
        def dfs(i, comb, node):
            if i == len(s):
                # last character needs to be the last character of word dict entry as well
                if node == trie:
                    # remove the last space
                    res.append(''.join(comb))
                return
            
            c = s[i]
            if c in node:
                if '*' in node[c]:
                    # we don't need space at the end
                    space = '' if i == len(s)-1 else ' '
                    comb.append(c + space)
                    dfs(i+1, comb, trie)
                    comb.pop()
                
                comb.append(c)
                dfs(i+1, comb, node[c])
                comb.pop()
            
        dfs(0, [], trie)
        return res


s = Solution()
print(s.wordBreak('catsanddog',['cat', 'cats', 'and', 'sand', 'dog']))
print(s.wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak(
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
