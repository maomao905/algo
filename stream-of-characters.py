"""
build trie O(WL)
when queried, if it matches trie, keep the matched node in list
at next query, iterate all the list and find the next match
query itself is O(N) for every node
if the node has end mark, return True

in worst, every query, we stack new node and query all nodes
O(L)

W: words length
L: longest word length
Q: num of queries
"""
from typing import List

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            node = self.trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            # end mark
            node['*'] = {}

        self.waiting = [self.trie]

    def query(self, letter: str) -> bool:
        new_waiting = []
        found = False
        for i in range(len(self.waiting)):
            node = self.waiting[i]
            if letter in node:
                if '*' in node[letter]:
                    found = True
                new_waiting.append(node[letter])
        
        self.waiting = new_waiting
        # start from the root of trie
        self.waiting.append(self.trie)
        return found

"""
reversed trie
dict = ['cde', 'f', kl]
stream = [a,b,c,d,e,f,g,h,i,j,k,l]

in normal trie, we have to store all possible paths
     root
   /   |   \
  c    f    k
  |         |
  d         l
  |
  e

in reversed trie, we don't need to store paths but just one pass to check if it matches
deque(l,k.j,i,h,g,f,e,d,c,b,a)
     root
   /   |   \
  e    f    l
  |         |
  d         k
  |
  c

same time and space complexity
"""
from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.max_len = 0
        for w in words:
            node = self.trie
            for c in reversed(w):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['*'] = {}
            self.max_len = max(self.max_len, len(w))
            
        self.stream = deque()
    
    def query(self, letter):
        self.stream.appendleft(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop()
        
        node = self.trie
        for c in self.stream:
            if '*' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '*' in node
        
        
streamChecker = StreamChecker(["cd","f","kl"]); # init the dictionary.
print(streamChecker.query('a'))          # return false
print(streamChecker.query('b'))          # return false
print(streamChecker.query('c'))          # return false
print(streamChecker.query('d'))          # return true, because 'cd' is in the wordlist
print(streamChecker.query('e'))          # return false
print(streamChecker.query('f'))          # return true, because 'f' is in the wordlist
print(streamChecker.query('g'))          # return false
print(streamChecker.query('h'))          # return false
print(streamChecker.query('i'))          # return false
print(streamChecker.query('j'))          # return false
print(streamChecker.query('k'))          # return false
print(streamChecker.query('l'))          # return true, because 'kl' is in the wordlist

# [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
# 
# [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,false,false,true,true,false,false]
# [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]
