# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get(self, root):
        if not root:
            return
        self.get(root.left)
        self.nums.append(root.val)
        self.get(root.right)
    def isValidBST(self, root: TreeNode) -> bool:
        self.nums=[]
        self.get(root)
        lens = len(self.nums)
        if lens == 1 or lens == 0:
            return True
        for i in range(lens-1):
            if self.nums[i] >= self.nums[i+1]:
                return False
        return True