class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def count_bit(n):
            c = 0
            while n > 0:
                c += n & 1
                n >>= 1
            return c
        
        def get_primes(n):
            p = [True] * (n+1)
            p[0] = p[1] = False
            for i in range(2,n+1):
                if not p[i]:
                    continue
                j = i*2
                while j <= n:
                    p[j] = False
                    j += i
            return p
        
        cnt = [0] * (R-L+1)
        for i in range(L,R+1):
            cnt[i-L] = count_bit(i)
        
        m = max(cnt)
        
        p = get_primes(m)
        ans = 0
        for c in cnt:
            if p[c]:
                ans += 1
        return ans
        
