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

    def insert(self, node, value):
        self.root.left = left
        self.root.right = right