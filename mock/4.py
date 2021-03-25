class Solution:
    def nextClosestTime(self, time: str) -> str:
        times = [int(t) for t in time if t.isdigit()]
        choices = set(times)
        
        def closest():
            for i in reversed(range(4)):
                if i == 1:
                    limit = 3 if times[0] == 2 else 9
                    mi = min([t for t in choices if times[i] < t <= limit], default=-1)
                    if times[i] < mi:
                        times[i] = mi
                        return True
                elif i == 3:
                    mi = min([t for t in choices if times[i] < t], default=-1)
                    if times[i] < mi:
                        times[i] = mi
                        return True
                elif i == 2:
                    mi = min([t for t in choices if 1 <= t <= 5 and times[i] < t], default=-1)
                    if times[i] < mi:
                        times[i] = mi
                        return True
                else:
                    mi = min([t for t in choices if 1 <= t <= 2 and times[i] < t], default=-1)
                    if times[i] < mi:
                        times[i] = mi
                        return True
            return False
        
        def get_ans(times):
            times = list(map(str, times))
            return ''.join(times[:2]) + ':' + ''.join(times[2:])
        
        if closest():
            return get_ans(times)
        else:
            res = [0] * 4
            choices = sorted(choices)
            for i in range(4):
                if i in (1,3):
                    res[i] = choices[0]
                elif i == 2:
                    for t in choices:
                        if 0 <= t <= 5:
                            res[i] = t
                            break
                else:
                    for t in choices:
                        if 0 <= t <= 2:
                            res[i] = t
                            break
            return get_ans(res)

s = Solution()
print(s.nextClosestTime('19:34'))
print(s.nextClosestTime('23:59'))
print(s.nextClosestTime('18:42'))
print(s.nextClosestTime('13:55'))
                    
                    
