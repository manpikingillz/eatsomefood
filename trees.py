'''
Implementing a tree.

1. Using Nodes and References:
---------------------------
- each tree node has a value and references to its child nodes.
- For binary trees, each node has a reference to its left and right child.
python

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

2. Using Arrays (especially for complete binary tees), not suitable for sparse trees.
-------------------------------------------------------------------------------------
- Useful for heap implementations
- If a node is at index i, its;
  -> left child is at index 2i+1
  -> left child is at index 2i+2

tree = [10, 5, 15, 2, 8, 12, 18] e.g 10, ->  5, 15, 5->2,8, 15->12,18


3. Using Edge Lists:
---------------------------

Maintain a list of edges where each edge represents a connection between two nodes.
More common in graph representations, but can be used for trees.
python
Copy code
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]

4. Using Adjacency Lists:
---------------------------

More common for general graphs but can be adapted for trees.
Each node indexes into a list, which then contains a list of its children.
python
Copy code
adjacency_list = [[1, 2], [3, 4], [], [], []]

5. Using Hash Maps/Tables:
---------------------------

Each node (key) maps to a list/set of its children.
python
Copy code
tree_map = {0: [1, 2], 1: [3, 4], 2: [], 3: [], 4: []}

6. Specialized Trees:
----------------------

-> B-Trees, B+ Trees: Used in databases and filesystems,
where nodes have variable numbers of child nodes within pre-defined range.
-> Trie (Prefix Tree): Each node represents a character of a string.
Commonly used in dictionary implementations.
-> Suffix Trees: For substring searches.
-> R-Trees: Used for spatial data structures.
-> Quad/Octrees: In graphics and spatial partitioning.

7. Immutable Trees:
----------------------
Trees that once created, cannot be altered. Any 'modification' results in a new tree.
Implemented using persistent data structures.
Useful in functional programming paradigms.

8. Flat Trees (like FlatBuffers or Protocol Buffers):
-----------------------------------------------------
Trees flattened to arrays, useful for serialization and deserialization
especially in systems with a focus on performance.
The choice of implementation often depends on:

9. Space and Time Complexities:
For insertions, deletions, searches, and traversals.

10. Use Cases:
Some trees (like Tries or AVL Trees) are better suited for specific problems.

11. Memory Overheads:
Space overhead of pointers in node-based trees vs. dense array representations.

12. Flexibility vs. Performance Trade-offs:
Dynamic structures (like node-based trees) are flexible, while static structures (like arrays) can be optimized for performance.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, parent_node: Node, left_value):
        if parent_node.left is None:
            parent_node.left = Node(left_value)
        else:
            new_node = Node(left_value)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node: Node, right_value):
        if parent_node.right is None:
            parent_node.right = Node(right_value)
        else:
            new_node = Node(right_value)
            new_node.right = parent_node.right
            parent_node.right = new_node

    def to_array(self):
        if not self.root:
            return []

        queue = [self.root]
        result = []

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result
    
    @classmethod
    def from_array(cls, arr):
        if not arr:
            return cls()
        
        root = Node(arr[0])
        tree = cls(root.value)
        queue = [root]
        idx = 1
        
        while queue and idx < len(arr):
            current_node = queue.pop(0)
            
            # Assign and enqueue the left child
            if idx < len(arr) and arr[idx] is not None:
                current_node.left = Node(arr[idx])
                queue.append(current_node.left)
            idx += 1
            
            # Assign and enqueue the right child
            if idx < len(arr) and arr[idx] is not None:
                current_node.right = Node(arr[idx])
                queue.append(current_node.right)
            idx += 1
        
        return tree


tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

print('tree: ', tree.to_array())

arr = [1, 2, 3, 4, 5]
tree1 = BinaryTree.from_array(arr)

print('from array: ', tree1)
