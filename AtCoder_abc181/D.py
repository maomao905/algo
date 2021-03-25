"""
1000が8で割り切れるので、
8の倍数であるかはlast three digitsを見ればわかる
ただし、2桁以下の数字の場合は逐一checkする
"""
from collections import Counter

num=input()

if len(num) <= 2:
    if int(num) % 8 == 0 or int(num[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
else:
    cnt = Counter(str(num))
    for i in range(8*13, 1000, 8):
        if len(Counter(str(i)) - cnt) == 0:
            print('Yes')
            exit()
    print('No')
    
        

        
