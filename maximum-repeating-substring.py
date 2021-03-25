class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        M=len(word)
        N=len(sequence)
        if M>N:
            return 0
        
        ans = 0
        for i in range(N):
            cnt = 0
            for j in range(i,N):
                k = (j - i) % M
                if sequence[j] == word[k]:
                    cnt += 1
                else:
                    break
            ans = max(cnt // M, ans)
        return ans

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        while word * k in sequence:
            k += 1
        return k-1

s = Solution()
print(s.maxRepeating('ababc', 'ab'))
print(s.maxRepeating('ababc', 'ba'))
print(s.maxRepeating('ababc', 'ac'))
print(s.maxRepeating('a', 'a'))
            
        
        
