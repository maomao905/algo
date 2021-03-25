from collections import defaultdict, deque, Counter

"""
V: number of vertices E: number of edges
time: O(V+E)
space: O(V+E)
"""

def topological_sort(vertices, edges):
  sorted_order = []
  if vertices <= 0:
      return sorted_order
  
  graph = defaultdict(list)
  in_degrees = Counter()
  
  
  ### keep the pair of parent and children in hash map
  ### keep the pair of node and the number of incoming edges in hash map
  # O(E)
  for edge in edges:
      graph[edge[0]].append(edge[1])
      in_degrees[edge[1]] += 1
  # print('in_degrees', in_degrees)
  
  ### keep track of source in queue
  ### if the node has 0 in_degrees, it is a source
  sources = [node for node in graph.keys() if node not in in_degrees]
  sources = deque(sources)
  
  """
  remove source from queue and decrement the in-degree and add new source in queue
  depth first search until sources become empty
  all nodes is appended to sources (queue) once, so while loop count equals V
  in-degrees is decremented until it is zero, which means number of edges E
  O(V+E)
  """
  while len(sources) > 0:
      # O(V) in total
      source = sources.popleft()
      sorted_order.append(source)
      children = graph[source]
      # O(E) in total
      for child in children:
          in_degrees[child] -= 1
          if in_degrees[child] == 0:
              sources.append(child)
  
  # topological sort is not possible as the graph has a cycle
  if len(sorted_order) != vertices:
      return []
              
  return sorted_order


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
