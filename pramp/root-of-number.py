def root(x, n):
  l, r = 0, x
  while l < r:
    mid = (l+r)/2
    m = mid ** n
    if abs(m - x) < 0.001:
      return mid
    if m > x:
      r = mid
    else:
      l = mid

print(root(7,3))
