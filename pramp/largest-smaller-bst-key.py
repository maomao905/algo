def find_largest_smaller_key(self, num):
    def dfs(node):
      if node is None:
        return -1
      
      if node.key < num:
        n = dfs(node.right)
        n = node.key if n == -1 else n
      else:
        n = dfs(node.left)

      return n if n is not None else node.key
    return dfs(self.root)
