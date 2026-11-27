# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        pu = deque([p])
        qu = deque([q])

        while pu and qu:
            p_node = pu.popleft()
            q_node = qu.popleft()
            if p_node.val != q_node.val:
                return False
            
            if p_node.left and q_node.left:
                pu.append(p_node.left)
                qu.append(q_node.left)
            elif not p_node.left and not q_node.left:
                x = 1
            else:
                return False
            
            if p_node.right and q_node.right:
                pu.append(p_node.right)
                qu.append(q_node.right)
            elif not p_node.right and not q_node.right:
                x = 1
            else:
                return False
        
        return True