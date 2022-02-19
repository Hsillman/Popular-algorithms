from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class HeightOfBinaryTree:
    def recursiveHeight(self, root: TreeNode)->int:
        '''
        - Recursive approach to return a Binary tree's height.
        - The time complexity of the algorithm is O(n) as we iterate through every node of 
            the binary tree calculating the height of the binary tree only once.
        - The space complexity is also O(n) as we are following recursion, where recursive stack 
            can have upto n elements. 
        '''
        def helper(root,depth=0):
            if not root:
                return depth
            else:
                return max(helper(root.left,depth+1),helper(root.right,depth+1))

        height_of_tree = helper(root)
        return height_of_tree

    def iterativeHeight(self, root: TreeNode)->int:
        '''
        - Breadth First Traversal implementation.
        - Time complexity is O(n). At most n elements in q.
        - Space complexity is O(n) as well.
        '''
        height = 0
        q = []
        if root:
            q.append(root)
        while q:
            aux = []
            height = height + 1
            for element in q:
                if element.left:
                    aux.append(element.left)
                if element.right:
                    aux.append(element.right)
            q = aux
        return height


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

s = HeightOfBinaryTree()
print("Height of a Binary Tree (Iterative):",s.iterativeHeight(root))
print("Height of a Binary Tree (Recursive):",s.recursiveHeight(root))
