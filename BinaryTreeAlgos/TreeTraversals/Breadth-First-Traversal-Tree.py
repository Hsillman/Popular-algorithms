from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BreadthFirstTraversal:
    """
    - This is the level order traversal. Prints the nodes by level.
    - Time complexity of O(n) where n is the number of nodes in the Tree.
    - Space complexity of O(n) because we use a queue. At maximum there will be n elements in queue.
    - BFS uses a queue unlike DFS, that uses a stack.
    """
    def iterativeBreadthFirstTraversal(self, root: TreeNode) -> List[int]:
        q = deque()
        visited = []
        if root:
            q.append(root)
        while q:
            popped_node = q.popleft()
            visited.append(popped_node.val)
            if popped_node.left:
                q.append(popped_node.left)
            if popped_node.right:
                q.append(popped_node.right)

        return visited
    

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7

s = BreadthFirstTraversal()
print("Breadth First Traversal (Iterative):",s.iterativeBreadthFirstTraversal(root))
