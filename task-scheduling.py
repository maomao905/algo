"""
we cannot schedule tasks if tasks have cyclic dependency
how can we detect cyclic dependency?
cyclic dependencyがある場合、in_degreesでsourcesに追加されないtaskが出てくる
なぜなら、in_degrees > 0で他のtaskが実行されないと、0にならないが、その他のtaskも他から参照されているため、deadlock
結果的に、最後のsourcesになったリストの数が全体のtask数と一致しているかを見れば良い

time: O(V+E)
space: O(V+E)
"""
from collections import defaultdict, Counter, deque
def is_scheduling_possible(tasks, prerequisites):
    graph = defaultdict(list)
    in_degrees = Counter()
    
    # create graph with hash map
    # create in-degrees counter
    # O(E)
    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degrees[child] += 1
    
    # extract sources
    sources = [parent for parent in graph.keys() if parent not in in_degrees]
    
    sources = deque(sources)
    
    scheduled_tasks = []
    
    while len(sources) > 0:
        # O(V)
        source = sources.popleft()
        scheduled_tasks.append(source)
        # O(E)
        for child in graph[source]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    
    return len(scheduled_tasks) == tasks
def main():
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 0], [2, 0]])))

main()
