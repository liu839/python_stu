# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get(self, root, deep):
        if not root: return
        try:
            self.res[deep].append(root.val)
        except IndexError:
            self.res.append([root.val])
        self.get(root.left, deep+1)
        self.get(root.right, deep+1)
    def judge(self, nums, reverse):
        lens = len(nums)
        if lens == 1 and not reverse:
            return nums[0]%2
        elif lens == 1 and reverse:
            return not nums[0]%2
        if reverse:
            for i in range(lens-1):
                if nums[i+1]>=nums[i] or nums[i]%2:
                    return False
        else:
            for i in range(lens-1):
                if nums[i+1]<=nums[i] or not nums[i]%2:
                    return False
        return True
    def isEvenOddTree(self, root: TreeNode) -> bool:
        self.res=[]
        self.get(root,0)
        flag = True
        for index in range(len(self.res)):
            flag = not flag
            if not self.judge(self.res[index]+[float("inf")] if not flag else self.res[index]+[float("-inf")], reverse=flag):
                return False
        return True