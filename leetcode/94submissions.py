# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        def cen(root,res):
            if root.left != None:
                cen(root.left,res)
                res.append(root.val)
            else:
                res.append(root.val)
            if root.right != None:
                cen(root.right,res)
        res = [ ]
        cen(root, res)
        return res
                