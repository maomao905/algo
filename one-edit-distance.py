class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        M,N=len(s),len(t)
        def helper(i,j,can_edit=True):
            if i == M and j == N:
                return not can_edit
            
            if i < M and j < N:
                if s[i] == t[j]:
                    return helper(i+1,j+1,can_edit)
            
            if not can_edit:
                return False
            if M<N:
                # insert
                return helper(i,j+1,False)
            elif M>N:
                # delete
                return helper(i+1,j,False)
            else:
                # replace
                return helper(i+1,j+1,False)
        
        return helper(0,0)

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        M,N=len(s),len(t)
        max_len = max(M,N)
        i = j = 0
        while i < max_len and j < max_len:
            if i < M and j < N and s[i] == t[j]:
                i+=1
                j+=1
                continue
            
            if M<N:
                # insert
                j+=1
            elif M>N:
                # delete
                i+=1
            else:
                # replace
                i+=1
                j+=1
            
            return s[i:] == t[j:]
            
        return False

s = Solution()
print(s.isOneEditDistance('ab','acb'))
print(s.isOneEditDistance('',''))
print(s.isOneEditDistance('a',''))
print(s.isOneEditDistance('','A'))
print(s.isOneEditDistance('abcdddd','abc'))
