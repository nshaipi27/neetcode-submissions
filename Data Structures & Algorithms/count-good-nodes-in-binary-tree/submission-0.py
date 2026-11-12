# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node, max_so_far):
            nonlocal good_nodes
            if max_so_far <= node.val:
                good_nodes += 1
                max_so_far = node.val
            if node.left:
                dfs(node.left, max_so_far)
            if node.right:
                dfs(node.right, max_so_far)
        dfs(root, root.val)
        return good_nodes