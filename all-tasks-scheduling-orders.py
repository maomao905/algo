from collections import defaultdict, deque, Counter

def sort_orders(tasks, prerequisites):
    # sources: [a, b, c]
    # N! combinations
    # pop a -> b -> c or a -> c -> b or b -> a -> c or b -> c -> a or c -> a -> b or c -> b -> a
    def backtrack(sources, sorted_order):
        for source in sources:
            sorted_order.append(source)
            # O(N)
            sources_copy = deque(sources)
            # only remove the current source
            # O(N)
            sources_copy.remove(source)
            
            for child in graph[source]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources_copy.append(child)
            
            backtrack(sources_copy, sorted_order)
            
            # backtrack
            # O(N)
            sorted_order.remove(source)
            for child in graph[source]:
                in_degrees[child] += 1
        
        # define the goal
        if len(sorted_order) == tasks:
            result.append(list(sorted_order))
        
        
    graph = defaultdict(list)
    
    in_degrees = Counter()
    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degrees[child] += 1
    
    sources = deque([parent for parent in graph.keys() if parent not in in_degrees])
    
    result = []
    backtrack(sources, [])
    
    return result
    

def main():
    print("Task Orders: ")
    print(sort_orders(3, [[0, 1], [1, 2]]))

    print("Task Orders: ")
    print(sort_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))

    print("Task Orders: ")
    print(sort_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))


main()
