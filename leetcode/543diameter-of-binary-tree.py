# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res.append(left+right)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res =[]
        self.dfs(root)
        return max(self.res)