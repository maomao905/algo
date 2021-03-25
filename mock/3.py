from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        r = c = 0
        
        i = 0
        N=len(sentence)
        ans = 0
        
        while r < rows:
            l = len(sentence[i])
            if l > cols:
                return 0
            
            if c + l - 1 >= cols:
                r += 1
                c = l-1
            else:
                c += l-1
            # print(sentence[i], (r, c))
            if i == N-1 and r < rows:
                ans += 1
            
            if c + 1 >= cols-1:
                c = 0
                r += 1
            else:
                c += 2
            
            i = (i + 1) % N
        return ans

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        N=len(s)
        start = 0
        
        for i in range(rows):
            start += cols
            if s[start % N] == ' ':
                start += 1
            else:
                while start > 0 and s[(start-1) % N] != ' ':
                    start -= 1
        return start // N
                    
s = Solution()
print(s.wordsTyping(['hello', 'world'], 2, 8))
print(s.wordsTyping(['a', 'bcd', 'e'], 3, 6))
print(s.wordsTyping(["I", "had", "apple", "pie"], 4,5))
print(s.wordsTyping(["f","p","a"],8,7)) # 10
# 0123456
# f_p_a_f
