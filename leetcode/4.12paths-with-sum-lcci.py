# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solv(self, root, res):
        if not root: return 0
        res = [root.val + each for each in res]+[root.val]
        return res.count(self.num) + self.solv(root.left, res) + self.solv(root.right, res)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.num = sum 
        return self.solv(root, [])
