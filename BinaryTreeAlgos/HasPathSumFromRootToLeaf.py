# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PathSum:
    def recursivepathSum(self, root: TreeNode,targetSum)->bool:
        '''
        - Checks if binary tree has root to leaf targetSum given by user.
        - The worst case is that we visit all nodes of this tree so the time complexity will be O(n).
        - This uses DFS logic.
        '''
        if not root:
            return False
        if (root.left == None) and (root.right == None) and targetSum == root.val:
            return True
       
        return self.recursivepathSum(root.left,targetSum - root.val) or self.recursivepathSum(root.right, targetSum - root.val)



    def iterativePathSum(self,root: TreeNode,targetSum)->bool:
        '''
        - Checks if binary tree has root to leaf targetSum given by user.
        - The worst case is that we visit all nodes of this tree so the time complexity will be O(n).
        - This uses DFS logic.
        - It uses 2 stacks so space complexity is higher compared to the recursive version
        '''
        stack = []
        sums = []
        if root:
            stack.append(root)
        sums.append(targetSum)
        while stack:
            popped_node = stack.pop()
            popped_sum = sums.pop()
            if (popped_node.val == popped_sum) and (popped_node.right == None) and (popped_node.left == None):
                return True
            new_sum = popped_sum - popped_node.val
            if popped_node.right:
                stack.append(popped_node.right)
                sums.append(new_sum)
            if popped_node.left:
                stack.append(popped_node.left)
                sums.append(new_sum)

        return False

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

s = PathSum()
print("This tree has the target sum provided? (Recurisve):",s.recursivepathSum(root,12))
print("This tree has the target sum provided? (Iterative):",s.iterativePathSum(root,12))