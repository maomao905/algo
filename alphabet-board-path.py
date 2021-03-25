"""
to handle z,
move left before moving down and move up before moving right
"""

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i, s in enumerate(board):
            for j, char in enumerate(s):
                pos[char] = (i,j)
        
        ans = []
        prev = (0,0)
        for c in target:
            cur = pos[c]
            
            path = []
            
            x = cur[0] - prev[0] if prev[0] < cur[0] else -(prev[0] - cur[0])
            xc = 'D' if x > 0 else 'U'
            for _ in range(abs(x)):
                path.append(xc)
            
            y = cur[1] - prev[1] if prev[1] < cur[1] else -(prev[1] - cur[1])
            yc = 'L' if y < 0 else 'R'
            for _ in range(abs(y)):
                path.append(yc)
            
            if path:
                if path[0] == 'D' and path[-1] == 'L':
                    path.reverse()
                elif path[0] == 'R' and path[-1] == 'U':
                    path.reverse()
            
            ans.extend(path)
            ans.append('!')
            prev = cur
        
        return ''.join(ans)

s = Solution()
print(s.alphabetBoardPath('leet'))
print(s.alphabetBoardPath('code'))
print(s.alphabetBoardPath('zdz'))
