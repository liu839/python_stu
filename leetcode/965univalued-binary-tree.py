# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def search(self, root, val):
        if not self :
            return
        if root.val != val:
            self.num = False
        if self.num:
            self.search(root.left, val)
            self.search(root.right, val)
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.num = False
        num = root.val
        self.search(root, num)
