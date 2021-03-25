"""
sliding window

save the visited characters and index in hash map and the current range(start index)
as long as there is we have unvisited characters, expand to the right
if visited character appear, we need to change the start index (shrink the window)
    'abcba' seen = {a: 0, b: 1, c: 2} start 0, then start = seen[b]+1 = 2
     ^  ^
    'baacdb' seen = {a: 2, b:0, c:3} start = 2, then start = 2 not seen[b]
       ^  ^
start = max(start, seen[char]+1)

time: O(N)
space: O(N) in worst
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        seen = {}
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                start = max(start, seen[char]+1)
            max_length = max(max_length, i-start+1)
            seen[char] = i
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring("devef"))
        
