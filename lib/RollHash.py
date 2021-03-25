A = 'abcd'
B = 'dacbabcdaacd'

W, MOD = 26, 2**32
L = len(A)

h = 0
for i in range(len(A)):
    h = (h * W + ord(A[i])) % MOD

b_h = 0
WL = pow(W,L,MOD)
for i in range(len(B)):
    if i < len(A):
        b_h = (b_h * W + ord(B[i])) % MOD
    else:
        b_h = (b_h * W - ord(B[i-L]) * WL + ord(B[i])) % MOD
    if b_h == h:
        return True


    
