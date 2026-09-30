# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stack = [(root, False)]
        heights = {None:0}

        while stack:
            node, visited = stack.pop()

            if visited:
                left_height = heights[node.left]
                right_height = heights[node.right]
                if abs(left_height - right_height) > 1:
                    return False
                heights[node] = 1 + max(left_height, right_height)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return True