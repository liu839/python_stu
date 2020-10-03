# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root):
        if not root:
            return 1
        self.deep[root.val] = max(self.search(root.left),self.search(root.right))
        return self.deep[root.val]+1
    def solv(self, root):
        while True:
            l = self.deep[root.left.val] if root.left else 0
            r = self.deep[root.right.val] if root.right else 0
            if l == r:
                return root
            if l > r :
                root = root.left
                continue
            if l < r :
                root = root.right
                continue
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.deep={}
        self.search(root)
        return self.solv(root)