"""
(()(()))
(
 () return 1
 (
  () return 1
 )
)
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        
        for s in S:
            if s == '(':
                stack.append(s)
            elif ')':
                r = 0
                while stack:
                    _s = stack.pop()
                    if _s == '(':
                        stack.append(max(1, r*2))
                        break
                    else:
                        r += _s
        return sum(stack)

"""
it's like tree structure
+1 for leaf node
child*2 for parent node

(()(())) -> (()) + ((()))
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = level = 0
        for i in range(len(S)):
            if S[i] == '(':
                level += 1
            else:
                # leaf node
                if S[i-1] == '(':
                    ans += 1 << level-1
                level -= 1
        return ans

s = Solution()
print(s.scoreOfParentheses('()'))
print(s.scoreOfParentheses('(())'))
print(s.scoreOfParentheses('()()'))
print(s.scoreOfParentheses('(()(()))'))
print(s.scoreOfParentheses('(()(()))()'))
