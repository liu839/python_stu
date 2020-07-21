 class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        if root == None:
            return []
        def read(root):
            if root == None:
                return []
            return read(root.left) + [root.val] + read(root.right)
        
        res = read(root)
        
        root = TreeNode(res[0])
        node = root
        for each in res[1:]:
            node.right = TreeNode(each)
            node = node.right
        return root
