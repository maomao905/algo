"""
- how to find first match
    - rolling hash

O(N)
"""
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        A,B = len(a),len(b)
        # calculate hash of a
        W, MOD = 26, 2**32
        WL = pow(W,A,MOD)
        
        a_h = 0
        for i in range(A):
            a_h = (a_h * W + ord(a[i])) % MOD
        
        def first_match():
            b_h = 0
            for i in range(B):
                if i < A:
                    b_h = (b_h * W + ord(b[i])) % MOD
                else:
                    b_h = (b_h * W - WL * ord(b[i-A]) + ord(b[i])) % MOD
                    
                if a_h == b_h:
                    return i
            return -1
        
        r = first_match()
        l = r-A+1
        if r == -1 or l >= A:
            if A*2>B:
                if b in a:
                    return 1
                if b in a*2:
                    return 2
            # print('--')
            return -1
        
        j = A-l
        # check first part
        for i in range(l):
            if A <= j or a[j] != b[i]:
                # print('!')
                return -1
            j += 1
        
        # check latter part
        for i in range(r+1, B):
            if a[(i-(r+1))%A] != b[i]:
                # print('--')
                return -1
        
        ans = 1
        if l > 0:
            ans += 1
        cnt, m = divmod(B-(r+1),A)
        # print(cnt,m)
        ans += cnt
        if m > 0:
            ans += 1
        return ans
        
s = Solution()
print(s.repeatedStringMatch('abcd', 'cdabcdab'))
print(s.repeatedStringMatch('a', 'aa'))
print(s.repeatedStringMatch('abc', 'wxyz'))
print(s.repeatedStringMatch('a', 'a'))
print(s.repeatedStringMatch('abc', 'bcabcabcabca'))
print(s.repeatedStringMatch('aa', 'a'))
print(s.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab","ba"))
print(s.repeatedStringMatch("abcd","bcdab")) # 2
print(s.repeatedStringMatch("baa","abaab")) # 3
print(s.repeatedStringMatch("aba","babbbbaabbababbaaaaababbaaabbbbaaabbbababbbbabaabababaabaaabbbabababbbabababaababaaaaabbabaaaabaaaab"
)) # 3
