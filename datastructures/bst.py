class Node:
    def __init__(self, key, value):
        self.key = key #key used for BST ordering
        self.value = value #associated value (e.g., stock price)
        self.left = None #left child node
        self.right = None #right child node

class BST:
    def __init__(self):
        self.root = None  #root node of the BST

    def insert(self, key, value): #insert new node or update existing node
        if not self.root:
            self.root = Node(key, value) #create root if empty
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key == node.key:
            node.value = value  #update value if key exists
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value) #insert left if empty
            else:
                self._insert(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value) #insert right if empty
            else:
                self._insert(node.right, key, value)

    def remove(self, key):
        self.root = self._remove(self.root, key) #remove node by key

    def _remove(self, node, key):
        if not node:
            return None #base case
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else: #found node to remove
            if not node.left:
                return node.right #replace node with right child
            if not node.right:
                return node.left #replace node with left child
            successor = self._min_value_node(node.right) #node with two children: find inorder successor
            node.key, node.value = successor.key, successor.value
            node.right = self._remove(node.right, successor.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left: #leftmost node is minimum
            current = current.left
        return current

    def inorder_traversal(self): #return sorted list 
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value)) #visit node
            self._inorder(node.right, result)

    def get_all_stocks_sorted(self): #wrapper for sorted stock list
        return self.inorder_traversal()


