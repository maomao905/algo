"""
Trie is n-ary
"""
class Node:
    def __init__(self, val=''):
        self.children = {}
        self.val = val
        self.is_end = False
    
    def get_next_node(self, char):
        return self.children.get(char)
    
    def add_child(self, node):
        self.children[node.val] = node
        
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        log(word length)
        """
        cur = self.root
        for char in word:
            node = cur.get_next_node(char)
            if node is None:
                node = Node(char)
                cur.add_child(node)
            
            cur = node
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        log(word length)
        """
        cur = self.root
        for char in word:
            cur = cur.get_next_node(char)
            if cur is None:
                return False
        
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        log(prefix length)
        """
        cur = self.root
        for char in prefix:
            cur = cur.get_next_node(char)
            if cur is None:
                return False
        
        return True

        


# Your Trie object will be instantiated and called as such:
trie = Trie();

print(trie.insert("apple"))
print(trie.search("apple"))   # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
print(trie.insert("app"))   
print(trie.search("app"))     # returns true
