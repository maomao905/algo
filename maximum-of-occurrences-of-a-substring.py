"""
O(N*(maxsize-minsize)^2)
"""
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N=len(s)
        res = Counter()
        def get_count(k):
            cnt = Counter()
            for i in range(N-k+1):
                if i == 0:
                    cnt = Counter(s[:k])
                else:
                    cnt[s[i-1]] -= 1
                    cnt[s[i+k-1]] += 1
                    if cnt[s[i-1]] == 0:
                        del cnt[s[i-1]]
                if len(cnt) <= maxLetters:
                    res[s[i:i+k]] += 1
        
        for k in range(minSize, maxSize+1):
            get_count(k)
        # print(res)
        return res.most_common(1)[0][1] if res else 0

"""
we only need to get count of min size because min size's count is always greater than count of max size
and when max size is satisfied, min size is always satisfied.
O(N*(max_size - min_size))
"""
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N=len(s)
        res = Counter()
        def get_count(k):
            cnt = Counter()
            for i in range(N-k+1):
                if i == 0:
                    cnt = Counter(s[:k])
                else:
                    cnt[s[i-1]] -= 1
                    cnt[s[i+k-1]] += 1
                    if cnt[s[i-1]] == 0:
                        del cnt[s[i-1]]
                if len(cnt) <= maxLetters:
                    res[s[i:i+k]] += 1
        
        get_count(minSize)
        return max(res.values()) if res else 0

"""
rolling hash
O(N)
"""
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N=len(s)
        W = 26
        MOD = 2**32
        freq = Counter()
        cnt = Counter()
        h = 0
        
        WL = pow(W, minSize, MOD)
        for i in range(N):
            if i < minSize:
                h = (h*W + ord(s[i]))%MOD
                cnt[s[i]] += 1
            else:
                h = (h*W - ord(s[i-minSize]) * WL + ord(s[i]))%MOD
                remove_char = s[i-minSize]
                cnt[remove_char] -= 1
                cnt[s[i]] += 1
                if cnt[remove_char] == 0:
                    del cnt[remove_char]
            
            if i >= minSize-1 and len(cnt) <= maxLetters:
                freq[h] += 1
        return max(freq.values(), default=0)
        
                
        

s = Solution()
print(s.maxFreq('aababcaab',2,3,4))
print(s.maxFreq('aaaa',1,3,3))
print(s.maxFreq('aabcabcab',2,2,3))
print(s.maxFreq('abcde',2,3,3))
            
