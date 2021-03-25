"""(WA)
W of S, T is subsequence of W
T <= W <= S
S = abcdebdde, T = bde (subsequence)
minimum substring W

- substring must contain all T's characters
- in order
"""
from collections import deque
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def get_next_pos():
            last = {}
            next_pos = [-1] * len(S)
            for i in reversed(range(len(S))):
                if S[i] in last:
                    next_pos[i] = last[S[i]]
            
                last[S[i]] = i
            return next_pos
        
        next_pos = get_next_pos()
        q = deque() # T's characters in the window (char, pointer of T, pointer of S)
        ans = ()
        
        for i in range(len(S)):
            # pointer of T
            j = q[-1][1] + 1 if q else 0
            if S[i] == T[j]:
                q.append([S[i], j, i])
            
            # window contains all T's characters
            while len(q) == len(T):
                # update minimum window length
                if not ans or ans[1] - ans[0] > q[-1][2] - q[0][2]:
                    ans = (q[0][2], q[-1][2])
                    print(q, ans)
                
                # shrink the window
                k = next_pos[q[0][2]]
                # it does not have first character of T later in S
                if k == -1:
                    return S[ans[0]:ans[1]+1]
                
                # remove old characters (out of range) in the window
                while q and q[0][2] > k:
                    q.pop()
        
        return S[ans[0]:ans[1]+1] if ans else ''

"""
O(ST)
"""
from collections import defaultdict
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        pos = defaultdict(list)
        for i in reversed(range(len(S))):
            pos[S[i]].append(i)
        
        pos = [list(pos[t]) for t in T]
        
        ans = ()
        while pos[0]:
            first = pos[0].pop()
            last = first
            for i in range(1, len(T)):
                while pos[i] and pos[i][-1] <= last:
                    pos[i].pop()
                if not pos[i]:
                    return S[ans[0]:ans[1]+1] if ans else ''
                
                last = pos[i][-1]

            if not ans or ans[1] - ans[0] > last - first:
                ans = (first, last)
        
        return S[ans[0]:ans[1]+1] if ans else ''
        
s = Solution()
print(s.minWindow('abcdebdde', 'bde'))
print(s.minWindow('abcdebde', 'bdde'))
print(s.minWindow('aabaaba', 'aaaaaaaa'))
