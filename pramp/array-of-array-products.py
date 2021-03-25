def array_of_array_products(arr):
  N=len(arr)
  if N <= 1:
    return []
  prefix = [1] * N
  for i in range(1,N):
    prefix[i] = prefix[i-1] * arr[i-1]
  
  suffix = [1] * N
  for i in reversed(range(N-1)):
    suffix[i] = suffix[i+1] * arr[i+1]
  
  return [prefix[i] * suffix[i] for i in range(N)]
