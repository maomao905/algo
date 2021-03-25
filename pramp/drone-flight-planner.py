def calc_drone_min_energy(route):
  cur = 0
  min_energy = 0
  N=len(route)
  for i in range(1,N):
    cur +=  route[i-1][2] - route[i][2]
    min_energy = min(min_energy, cur)
    
  return -min_energy
  
"""
simpler solution
"""
def calc_drone_min_energy(route):
    first_height = route[0][2]
    max_height = max(map(lambda x: x[2], route))
    return max_height - first_height
      
# route = [[0,2,10],[3,5,0],[9,20,6],[10,12,15],[10,10,8]]
route = [[0,1,19]]


print(calc_drone_min_energy(route))
