import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def from_read(dtype=np.int64):
    r = """
1 1
2 3
2 2
"""
    return np.fromstring(r, dtype=dtype, sep=' ')


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')

# @njit((i8, i8, i8[:, :], i8[:, :]), cache=True)
def main(H, W, AB, CD):
    G = np.zeros((H, W), np.int64)
    # light bulb
    for i in range(len(AB)):
        a, b = AB[i]
        G[a - 1, b - 1] = 1
    # block
    for i in range(len(CD)):
        c, d = CD[i]
        G[c - 1, d - 1] = -1
    res = np.zeros((H, W), np.bool_)  # 光ったマス (bool)
    for _ in range(4):
        res, G = res.T[::-1], G.T[::-1]
        # 下方向に解く
        A = np.zeros_like(res) # すべてfalseで初期化
        H, W = A.shape
        for h in range(H):
            if h >= 1:
                # use memorization
                A[h] |= A[h - 1] # ひとつ手前が光っていたら、現在地点も光ってる
            A[h][G[h] == 1] = 1 # 1を代入したらTrueが入る
            A[h][G[h] == -1] = 0  # 0を代入したらFalseが入る
        res |= A
    return np.sum(res)

# H, W, N, M = map(int, readline().split())
H, W, N, M = 3,3,2,1
nums = from_read()
AB = nums[:N + N].reshape(N, 2)
CD = nums[N + N:].reshape(M, 2)

print(main(H, W, AB, CD))
