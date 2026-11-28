# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root)[k - 1]
        
    def dfs(self, root):
        if not root:
            return []

        result = self.dfs(root.left)
        result.append(root.val)
        result.extend(self.dfs(root.right))

        return result