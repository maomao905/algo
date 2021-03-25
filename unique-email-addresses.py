"""
time: O(N*M) n is the length of emails and M is the length of email
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            _email = email.split('@')
            local, domain = _email[0], _email[1]
            if '+' in local:
                idx = local.index('+')
                local = local[:idx]
            local = local.replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)

s = Solution()
print(s.numUniqueEmails(
    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
))
            
            
        
