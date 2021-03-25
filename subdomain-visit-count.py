"""
M subdomain per cpdomain
L length of each domain
ML for hashing
O(NML) = O(100*100*3) = O(30000)
"""
from typing import List
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for website in cpdomains:
            count, domain = website.split()
            domains = domain.split('.')
            for i in range(len(domains)):
                cnt['.'.join(domains[i:])] += int(count)
        
        return [f'{count} {domain}' for domain, count in cnt.items()]

s = Solution()
print(s.subdomainVisits(['9001 discuss.leetcode.com']))
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
