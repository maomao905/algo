"""
we can insert one letter in any position
    -> we can sort
    ['a', 'b', 'ab', 'abc', 'abd', 'abcd']

trie
    {
        'a': {
            'b'
        },
        'b': {
            ''
        }
    }
    -> does not work because word is sorted if given [b, ba] we cannot go down in trie b -> ab
    if we need to keep all possible combinations of each word in trie
    DFS trie and count the end mark and get the max count
    
brute-force
from word of shortest length to word of longest length, greedy search
keep length key in hash map
{
  1: ['a', 'b']
  2: ['ab']
}
after 'a', we check the words of length 2, if 'a' is contained, check the words of length 3...
if any word does not match, then reset the count start next length of word 
O(N^2*L) L: maximum word length
use memorization memo[word] = count

delete once character from word
abcd -> [abc, abd, acd, bcd]
if there is a match of these words, there is a path
-> how about store all words in hash map O(N) and check if one-letter-deleted word match in the map
then, we can create a graph where a vertex represents a word and an edge represents a connection (bc -> bca) O(N*L^2)
    - string concatnation O(L)
    - delete L times
    - N times
then, DFS from every node (every word) O(N^2) in worst (every node has N paths at most)
but it is actually not O(N^2) because it is total number of edges, which is O(NL) as I created above

in total, O(NL^2 + N^2) -> O(NL^2 + NL) -> O(NL^2)
"""

from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        def dfs(start):
            if start not in graph:
                return 1
            
            if start in memo:
                return memo[start]
            
            max_cnt = 0
            for i in graph[start]:
                max_cnt = max(max_cnt, 1 + dfs(i))
                # print(i, max_cnt)
            
            # max count of start to the end
            memo[start] = max_cnt
            return max_cnt
            
        word_to_idx = {word: idx for idx, word in enumerate(words)}
        graph = defaultdict(set)
        
        # build a graph, there is an edge if word which one letter is deleted matches another word
        for i, word in enumerate(words):
            for j in range(len(word)):
                one_letter_deleted = word[:j] + word[j+1:]
                if one_letter_deleted in word_to_idx:
                    graph[word_to_idx[one_letter_deleted]].add(i)
        
        # print(graph)
        max_cnt = 0
        # DFS
        for i in range(len(words)):
            max_cnt = max(max_cnt, dfs(i))
        # print(memo)
        return max_cnt

"""
DP

a -> ba -> bda -> bdca
1    2      3      4
dp[ba] = dp[a] + 1
dp[bda] = dp[ba] + 1...

if one-letter-deleted word exist in dp table, then we can plus one with it
but, we need to start from the shortest-length word, otherwise, it does not hit in dp table
-> sort by length O(NlogN)
-> DP O(N*L^2)
    - delete one-letter N*L times
    - string concatnation and hashing O(L)
-> overall, O(N*L^2 + NlogN)
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                one_letter_deleted = word[:i] + word[i+1:]
                if one_letter_deleted in dp:
                    dp[word] = max(dp[word], dp[one_letter_deleted] + 1)
        
        return max(dp.values())

s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
