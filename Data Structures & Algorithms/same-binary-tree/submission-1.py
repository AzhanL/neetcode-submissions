# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = deque() 
        stack_q = deque()

        if p:
            stack_p.append(p)
        if q:
            stack_q.append(q)
        
        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
            
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
            elif node_p is None and node_q is None:
                continue 
            else:
                return False
        
        return not stack_p and not stack_q