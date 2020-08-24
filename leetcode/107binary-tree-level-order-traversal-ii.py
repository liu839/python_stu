# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getval(self, root, deep):
        if not root:
            return
        try:
            self.res[deep].append(root.val)
        except IndexError:
            self.res.append([root.val])
        self.getval(root.left, deep+1)
        self.getval(root.right, deep+1)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.getval(root, 0)
        self.res.reverse()
        return self.res
