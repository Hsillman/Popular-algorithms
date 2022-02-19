'''
Pre-Order, Post-Order and In-Order are all variations of Depth First Traversals
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PreOrderTraversal:
    def iterativePreOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - O(n) time complexity. Every node is popped from the stack once.
        - O(n) space complexity. At most n elements in stack.
        - This is a classic implementation of DepthFirstTraversal. Notice that,
          if we simply change the order of the if's "visited.right" and "visited.left"
          we get a depth first traversal that travels first to the right subtree instead
          of the left subtree
        - This is a Pre-Order traversal.
        '''
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack:
            visited = stack.pop()
            if visited.right:
                stack.append(visited.right)
            if visited.left:
                stack.append(visited.left)
            result.append(visited.val)
        return result

    def recursivePreOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - O(n) time complexity because of n calls made to visit the whole Tree.
        - O(n) space complexity because of the call stack.
        - This is a Pre-Order traversal.
        '''
        result = []
        def PreOT(root):
            if root:
                result.append(root.val)
                PreOT(root.left)
                PreOT(root.right)
        
        PreOT(root)
        return result


class PostOrderTraversal:
    def iterativePostOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - O(n) time complexity because one of the stacks has a maximum of n values.
        - O(n) space complexity because in a stack will ocuppy n positions in memory.
        - This is a Post-Order traversal.
        '''
        stack1 = []
        stack2 = []
        if root:
            stack1.append(root)
        while stack1:
            popped_node = stack1.pop()
            stack2.append(popped_node.val)
            if popped_node.left:
                stack1.append(popped_node.left)
            if popped_node.right:
                stack1.append(popped_node.right)
        #stack2 will have the result, but backwards        
        return stack2[::-1]

    def recursivePostOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - O(n) time complexity because of n calls made to visit the whole Tree.
        - O(n) space complexity because of the call stack.
        - This is a Post-Order traversal.
        '''
        result = []
        def PostOT(root):
            if root:
                PostOT(root.left)
                PostOT(root.right)
                result.append(root.val)

        PostOT(root)
        return result


class InOrderTraversal:
    def recursiveInOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - O(n) time complexity because of n calls made to visit the whole Tree.
        - O(n) space complexity because of the call stack.
        - This is a In-Order traversal.
        '''
        result = []
        def InOT(root):
            if root:
                InOT(root.left)
                result.append(root.val)
                InOT(root.right)

        InOT(root)
        return result

    def iterativeInOrderTraversal(self, root: TreeNode) -> List[int]:
        '''
        - This is not the most optimize implementation but it does the trick.
        - O(n) time complexity because you have to go through all the nodes and put them in a stack.
        - O(n) space complexity, at most n elements in a stack.
        - This is a In-Order Traversal.
        '''
        stack1 = []
        stack2 = []
        if root:
            stack1.append(root)
        
        while stack1:
            if stack1[-1].right and (stack1[-1].right not in stack2):
                stack1.append(stack1[-1].right)
            else:
                popped_node = stack1.pop()
                if popped_node.left:
                    stack1.append(popped_node.left)
                stack2.append(popped_node)

        while stack2:
            stack1.append(stack2.pop().val)
        return stack1


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
s = PreOrderTraversal()
print("Pre-Order Traversal (Iterative):", s.iterativePreOrderTraversal(root))
print("Pre-Order Traversal (Recursive):", s.recursivePreOrderTraversal(root))

s = PostOrderTraversal()
print("Post-Order Traversal (Iterative):", s.iterativePostOrderTraversal(root))
print("Post-Order Traversal (Recursive):", s.recursivePostOrderTraversal(root))

s = InOrderTraversal()
print("In-Order Traversal (Iterative):", s.iterativeInOrderTraversal(root))
print("In-Order Traversal (Recursive):", s.recursiveInOrderTraversal(root))
