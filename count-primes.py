"""
2 
3 3 % 2 = 1  prime
4 4 % 2 = 0  not prime
5 5 % 2 = 1
  5 % 3 = 2  prime
6 6 % 2 = 0  not prime
...

if we can divide by all primes up to N and have no remainder, then N is not prime,
time: O(N^2) -> TLE
space: O(N)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        primes = [2]
        
        def is_prime(i):
            for p in primes:
                if i % p == 0:
                    return False
            return True
        
        for i in range(3, n):
            if is_prime(i):
                primes.append(i)
        
        return len(primes)

"""
if we find prime, we can multiply prime up to N, then, we don't have to check multiplied numbers, since it's not prime
we dont' have to check more than sqrt(N)
N=100, sqrt(10) -> 11 * 2, 11 * 3... 11 * 10 is already check by lower number and 11 * 11 is always more than N
range is prime * prime < N
time: O(N)
space: O(N)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * (n)
        if n < 3:
            return 0
        
        
        for i in range(2, int(n ** 0.5)+1):
            if not prime[i]:
                continue
            
            for j in range(i*i, n, i):
                prime[j] = False
        
        # exclude 0 and 1
        return prime.count(True) - 2

s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(12))
print(s.countPrimes(0))
print(s.countPrimes(2))
print(s.countPrimes(3))
