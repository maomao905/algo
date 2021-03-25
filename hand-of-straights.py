from typing import List
from collections import defaultdict, Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        cards = defaultdict(list)
        for c in hand:
            if cards[c]:
                count = cards[c].pop()
            else:
                count = 1
            if count != W:
                cards[c+1].append(count+1)
        return all(len(count_list)==0 for count_list in cards.values())

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = Counter(hand)
        for n in sorted(cnt):
            for _ in range(cnt[n]):
                for i in range(n, n+W):
                    if cnt[i] <= 0:
                        return False
                    cnt[i] -= 1
        return True

"""
O(MlogM + MW)
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = Counter(hand)
        for n in sorted(cnt):
            if cnt[n] == 0:
                continue
            need = cnt[n]
            for i in range(n, n+W):
                cnt[i] -= need
                if cnt[i] < 0:
                    return False
        return True
        
s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(s.isNStraightHand([1,2,3,4,5], 4))
print(s.isNStraightHand([1,2,3], 1))
print(s.isNStraightHand([2,1], 2))
print(s.isNStraightHand([1,2,1,2,3,3], 3))
                
