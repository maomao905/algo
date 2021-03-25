"""

BFS because simultaneously pushing dominoes

keep timestamp in the array
.L.R...LR..L..
(0,.)(0,L)(0,.)(0,R)(0,.)(0,.)(0,.)(0,L)(0,R)(0,.)(0,.)(0,L)(0,.)(0,.)
(1,L)(0,L)(0,.)(0,R)(1,R)(0,.)(1,L)(0,L)(0,R)(1,R)(1,L)(0,L)(0,.)(0,.)
(1,L)(0,L)(0,.)(0,R)(1,R)(2,.)(1,L)(0,L)(0,R)(1,R)(1,L)(0,L)(0,.)(0,.)

- we can only fall '.' domino any time
- except when time is the same and opposite direction
time O(N) space O(N)
"""

from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N=len(dominoes)
        if not N:
            return ''
        
        d = [None] * N
        q = deque()
        for i in range(N):
            if dominoes[i] in 'LR':
                q.append(i)
            n = 0
            if dominoes[i] == 'L':
                n = -1
            elif dominoes[i] == 'R':
                n = 1
            d[i] = (0, n)
        
        t = 0
        while q:
            t += 1
            for _ in range(len(q)):
                i = q.popleft()
                
                move = d[i][1]
                if not(0 <= i+move < N):
                    continue
                
                next_move = d[i+move][1]
                if next_move == 0 or (next_move == -move and d[i+move][0] == t):
                    next_move += move
                    d[i+move] = (t, next_move)
                    if next_move:
                        q.append(i+move)
            
        
        for i in range(N):
            move = d[i][1]
            if move == -1:
                d[i] = 'L'
            elif move == 1:
                d[i] = 'R'
            else:
                d[i] = '.'
        
        return ''.join(d)
            
s = Solution()            
print(s.pushDominoes('.L.R...LR..L..'))
print(s.pushDominoes('RR.L'))
            
