"""
1. brute-force O(WS)

for w in words: O(W)
    check if w is subsequence of s O(S)

2. looking at only next character of words
words = ['a', 'bb', 'acd', 'ace']
S = 'abcde'
     ^
after 'a' appears in S, we can delete all 'a' from words
words = ['', 'bb', 'cd', 'ce']

we keep pointers where we look at in each word
in order to avoid check all words every time,
we use hash map and to store next target character and index of words
{
 'a': [0, 2, 3],
 'b': [1]
}
after matching the character, we replace it with new character of the word

time: O(WL + S)
space: O(W)
"""
from typing import List
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        W=len(words)
        # which character we are looking at for each word
        w_ptr = [0] * W
        # character and word index pair
        hm = defaultdict(list)
        
        for i, w in enumerate(words):
            hm[w[0]].append(i)
        
        cnt = 0
        for s in S:
            if s not in hm:
                continue
            
            idx_list = hm[s]
            del hm[s]
            
            for word_idx in idx_list:
                w_ptr[word_idx] += 1
                word = words[word_idx]
                char_idx = w_ptr[word_idx]
                
                if char_idx >= len(word):
                    cnt += 1
                    continue
                
                hm[word[char_idx]].append(word_idx)
                
            if len(hm) == 0:
                break
        return cnt

s = Solution()
print(s.numMatchingSubseq('abcde', ['a', 'bb', 'acd', 'ace']))
                
        
