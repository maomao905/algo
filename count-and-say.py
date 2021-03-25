class Solution:
    def countAndSay(self, n: int) -> str:
        cur = ['1']
        for i in range(n-1):
            j = 0
            res = []
            while j < len(cur):
                cnt = 1
                while j+1<len(cur) and cur[j] == cur[j+1]:
                    j+=1
                    cnt += 1
                res.extend([str(cnt),cur[j]])
                j += 1
            cur = res
        return ''.join(cur)
