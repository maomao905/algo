"""
(TLE)
check every index as start index and expand the substring and check it's valid and update the maximum length if it's valid
O(N^2) N indices x N substring

how to check substring is valid
use hash map and count the frequency to check if freq >= k
s is only lowercase English letters, which is size of 26, which is O(1)
"""
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_length = 0
        N=len(s)
        # i is start index of substring
        for i in range(N):
            cnt = Counter()
            # j is the end of substring
            for j in range(i, N):
                cnt[s[j]] += 1
                if min(cnt.values()) >= k:
                    max_length = max(max_length, j-i+1)
        return max_length

"""
(WA)
binary search
binary search length of longest substring
if the longest substring with the length exists, increase the length
in every length, we check it's valid using counter in the same way as above O(1) * O(N-k)
O(NlogN)

-> it does not work because length A of substring is not valid but length B of substring is valid when A < B
so, we cannot simply binary search based on the length
e.g.) abababa k=3
abab (length 4) is not valid but ababab (length 6) is valid, while length of 7 is not valid
"""
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def length_exist(size):
            cnt = Counter(s[:size])
            for start in range(N-size):
                if min(cnt.values()) >= k:
                    return True
                cnt[s[start]] -= 1
                cnt[s[start+size]] += 1
            return False
        
        N=len(s)
        l = k
        r = N
        
        while l < r:
            mid = l + (r-l) // 2
            if length_exist(mid):
                l = mid
            else:
                r = mid-1
        return l

"""
(TLE)
store invalid chars in hash set
if we know [i..j] is valid, if j+1 is valid, [i..j+1] is valid
but if [i..j] is not valid, we cannot know [i..j+1] is valid easily
-> maybe we should check backward
because we know the frequency of each character if we start from the end
we also need to keep invalid chars in hash map
if there is no invalid chars, it's valid and increment the frequency counter
if there is invalid chars, check the target chars in invalid chars and increment the frequency counter
and check it's valid now, if it's valid, remove the char from invalid map and if the length of invalid map is 0,
it's valid
"""
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        N=len(s)
        max_len = 0
        
        for i in range(N):
            invalid_chars = set()
            cnt = Counter()
            for j in range(i,N):
                cnt[s[j]] += 1
                if cnt[s[j]] < k:
                    invalid_chars.add(s[j])
                elif s[j] in invalid_chars:
                    invalid_chars.remove(s[j])
                
                if len(invalid_chars) == 0:
                    max_len = max(max_len, j-i+1)
                # print(cnt, invalid_chars)
        return max_len

"""
if we find an invalid char which frequency is less than k,
there is a valid substring before or after the invalid char
aaabbccc k=3
{a: 3, b:2, c:3} -> b is invalid
valid substring exists before b or after b
time: O(N^2)
"""
from collections import Counter
class Solution:
    def is_valid(self, cnt, k):
        for s, count in cnt.items():
            if count < k:
                return False, s
        return True, ''
        
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        cnt = Counter(s)
        valid, invalid_char = self.is_valid(cnt, k)
        if valid:
            return len(s)
        max_len = 0
        prev = 0
        for i, char in enumerate(s):
            if char == invalid_char:
                # print(prev, i)
                length = self.longestSubstring(s[prev:i], k)
                max_len = max(max_len, length)
                prev = i+1
        if prev < len(s):
            length = self.longestSubstring(s[prev:len(s)], k)
            max_len = max(max_len, length)
        return max_len

"""
this solution is very complicated when you implement
sliding window based on number of unique chars
longest substring contains U characters at most
U is the number of unique characters in s
so, from 1 to U, we search one by one
s = aabcbacad k=2
unique chars = {a,b,c,d}, thus the range of unique chars in longest substring is 1 ~ 4

O(26) at most
for num_of_unique_chars in range(4):
    # sliding window O(N)
    if current num of unique chars exceeds num_of_unique_chars, shrink the window
    and if it is less than num of unique chars, expand it
time: O(N)
space: O(1) only counter of english letters
"""
from collections import Counter
class Solution():
    def longestSubstring(self, s, k):
        max_unique_chars = len(set(s))
        
        max_len = 0
        for num_unique_chars in range(1, max_unique_chars+1):
            cnt = Counter()
            valid_char_cnt = 0
            
            l = r = 0
            while r <= len(s):
                # expand the window
                if len(cnt) <= num_unique_chars:
                    if len(cnt) == num_unique_chars and valid_char_cnt == len(cnt):
                        # print(num_unique_chars, cnt, valid_char_cnt, r,l)
                        max_len = max(max_len, r-l)
                    if r < len(s):
                        cnt[s[r]] += 1
                        if cnt[s[r]] == k:
                            valid_char_cnt += 1
                    r += 1
                # shrink the window
                else:
                    if cnt[s[l]] == k:
                        valid_char_cnt -= 1
                    cnt[s[l]] -= 1
                    if cnt[s[l]] == 0:
                        del cnt[s[l]]
                    l += 1
        return max_len

s = Solution()
print(s.longestSubstring('aaabb', 3))
print(s.longestSubstring('aaabbb', 3))
print(s.longestSubstring('ababbc', 2))
print(s.longestSubstring('aaa', 5))
