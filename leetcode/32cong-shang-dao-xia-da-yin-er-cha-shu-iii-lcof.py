# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.search(root,0)
        for i in range(len(self.res)):
            if i%2:
                self.res[i] = list(reversed(self.res[i]))
        return self.res
    def search(self, root, deep):
        if not root:
            return
        try:
            self.res[deep].append(root.val)
        except :
            self.res.append([root.val])
        self.search(root.left, deep+1)
        self.search(root.right, deep+1)
