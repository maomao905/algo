"""
deque

- fix one alphabet(A) and get the length of repeating A
- we can at most k different characters inside the window
AAxAAAxx (when k=3 and x is different character)

time: O(N)
"""

from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        N=len(s)
        for char in set(s):
            cands = deque()
            l = 0
            for r in range(N):
                if s[r] != char:
                    # candidate to replace with char
                    cands.append(r)
                    # we cannot replace more than k, so we move the left pointer
                    if len(cands) > k:
                        cand = cands.popleft()
                        l = cand + 1
                max_len = max(max_len, r-l+1)
        return max_len

"""
two pointers in one pass
we tried all 26 letters separately in above approach
but we don't have to do it

window size is length of most frequent character + k
<--- most frequent character size ---><-- k (any other character)-->

window_end - window_start + 1 = max_count + k
while window_end - window_start + 1 > max_count + k:
    we need to shrink the window
    decrease the count of character at window_start position

max_length = max(window_end - window_start)

time: O(N) space: O(N)
"""

from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # counter of characters which appear within the window
        cnt = Counter()

        window_start = 0
        # count of most frequent character within the window
        max_count = 0

        for window_end in range(len(s)):
            cnt[s[window_end]] += 1
            max_count = max(cnt[s[window_end]], max_count)

            """
            this condition is true only when s[window_end] is not most frequent character
            because if it's most frequent, max_count is also updated and window_size is also updated by one

            we don't have to update max_count because our goal is to find the max window size
            we just keep at least the max_count + k size as the max window size till the end
            """
            if window_end - window_start + 1 > max_count + k:
                cnt[s[window_start]] -= 1
                window_start += 1

        return len(s) - window_start
            
s = Solution()
print(s.characterReplacement('ABAB', 2))
print(s.characterReplacement('AABABBA', 1))
print(s.characterReplacement('BBBABABBBABBBBABB', 2))
print(s.characterReplacement('CCDCACBB', 2))
