# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], current=0) -> int:
        if not root:
            return current

        current += 1
        left = self.maxDepth(root.left, current) if root.left else current
        right = self.maxDepth(root.right, current) if root.right else current
        
        return max(left, right)