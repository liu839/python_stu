# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSame(self, s: TreeNode, t: TreeNode) -> bool:
        if s == t == None:
            return True
        elif s == None and t != None or s != None and t == None:
            return False
        else:
            if s.val == t.val:
                return self.isSame(s.left, t.right) and self.isSame(s.right, t.left)
            else:
                return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSame(root.left, root.right)
