# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        most = 0
        last = None
        cnt = 0
        def inorder(node):
            if not node:
                return
            nonlocal ans, most, last, cnt
            inorder(node.left)
            cnt = 1 if node.val != last else cnt + 1
            if cnt == most:
                ans.append(node.val)
            elif cnt > most:
                most = cnt
                ans = [node.val]
            last = node.val
            inorder(node.right)
        inorder(root)
        return ans