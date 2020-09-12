# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root, deep):
        if not root:
            return
        try:
            self.res[deep].append(root.val)
        except:
            self.res[deep]=[root.val]
        self.search(root.left, deep+1)
        self.search(root.right, deep+1)
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        self.res=[]
        self.search(root, 0)
        self.res = [sum(each)/len(each) for each in self.res]
        
