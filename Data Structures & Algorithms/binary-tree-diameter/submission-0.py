# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        max_height = {}
        diameter = 0

        while stack:
            node, visited = stack.pop() 
            if not visited:
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
                if node.right: stack.append((node.right, False))
            else:
                if node.left is None:
                    left_height = 0
                else:
                    left_height = max_height.pop(node.left)
                
                if node.right is None:
                    right_height = 0
                else:
                    right_height = max_height.pop(node.right)
                
                diameter = max(diameter, right_height + left_height)
                max_height[node] = max(right_height, left_height) + 1
        return diameter