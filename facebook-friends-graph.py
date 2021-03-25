import threading, queue
"""
- find_path_bi_BFS
- searchLevel # search one level
- mergePath # searches met at connection
class PathNode
    - person
    - previousNode
    - collapse()
class BFSData
    - toVisit (queue) これからvisitするnode
    - visited (hash) visitしたnode
"""
queue = []
append, pop(0)
