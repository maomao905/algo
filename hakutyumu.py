"""
- dream, dreamer, erase, eraser
erasedream
    - erase + dream
dreameraser
    - dreamer + eraser
        - erで始まる場合、dreamer or eraser
traverse backwards
dream + er, erase + er
"""
S=input()
# S= 'dreameraser'

while True:
    for word in ('dream', 'dreamer', 'erase', 'eraser'):
        # print(S.endswith(word), word)
        if S.endswith(word):
            S = S[:-len(word)]
            break
    else:
        # print('S is', S)
        print('NO')
        break
    
    # print(S)
    if not S:
        print('YES')
        break
